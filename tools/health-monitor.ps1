# Health Monitor Script for Rabbit
# Checks: Event logs, SSD health, recent crashes, temps

$report = @{
    timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    issues = @()
    warnings = @()
    stats = @{}
}

# Check HWiNFO temps if log exists
$hwLog = "C:\Users\Grant\Documents\logs\logs.CSV"
if (Test-Path $hwLog) {
    try {
        $lastLine = Get-Content $hwLog -Tail 1
        $headers = (Get-Content $hwLog -Head 1) -split ','
        $values = $lastLine -split ','
        
        # Find temp columns (CPU Tctl/Tdie, GPU Temp, GPU Hotspot)
        for ($i = 0; $i -lt $headers.Count; $i++) {
            $h = $headers[$i].Trim('"')
            $v = $values[$i]
            
            if ($h -match 'CPU \(Tctl/Tdie\)' -and $v -match '[\d.]+') {
                $temp = [double]$v
                $report.stats.cpuTemp = $temp
                if ($temp -gt 85) { $report.issues += "CPU TEMP: ${temp}C - CRITICAL" }
                elseif ($temp -gt 75) { $report.warnings += "CPU TEMP: ${temp}C - elevated" }
            }
            if ($h -eq '"GPU Temperature [°C]"' -or $h -eq 'GPU Temperature [�C]') {
                if ($v -match '[\d.]+') {
                    $temp = [double]$v
                    $report.stats.gpuTemp = $temp
                    if ($temp -gt 85) { $report.issues += "GPU TEMP: ${temp}C - CRITICAL" }
                    elseif ($temp -gt 80) { $report.warnings += "GPU TEMP: ${temp}C - elevated" }
                }
            }
            if ($h -match 'GPU Hot Spot') {
                if ($v -match '[\d.]+') {
                    $temp = [double]$v
                    $report.stats.gpuHotspot = $temp
                    if ($temp -gt 100) { $report.issues += "GPU HOTSPOT: ${temp}C - CRITICAL" }
                    elseif ($temp -gt 90) { $report.warnings += "GPU HOTSPOT: ${temp}C - elevated" }
                }
            }
        }
    } catch {
        $report.warnings += "HWINFO: Could not parse log"
    }
}

# Check for unexpected shutdowns in last 24 hours
$crashes = Get-WinEvent -FilterHashtable @{LogName='System'; Id=6008; StartTime=(Get-Date).AddHours(-24)} -ErrorAction SilentlyContinue
if ($crashes) {
    $report.issues += "CRASHES: $($crashes.Count) unexpected shutdown(s) in last 24h"
    $report.stats.recentCrashes = $crashes.Count
}

# Check for WHEA hardware errors
$whea = Get-WinEvent -FilterHashtable @{LogName='System'; ProviderName='Microsoft-Windows-WHEA-Logger'; StartTime=(Get-Date).AddHours(-24)} -ErrorAction SilentlyContinue
if ($whea) {
    $report.issues += "HARDWARE: $($whea.Count) WHEA error(s) - possible hardware failure"
    $report.stats.wheaErrors = $whea.Count
}

# Check SSD health
$disks = Get-PhysicalDisk | Where-Object { $_.HealthStatus -ne 'Healthy' }
if ($disks) {
    foreach ($d in $disks) {
        $report.issues += "DISK: $($d.FriendlyName) health is $($d.HealthStatus)"
    }
}

# Check disk space
$volumes = Get-Volume | Where-Object { $_.DriveLetter -and $_.SizeRemaining -lt 10GB -and $_.Size -gt 0 }
foreach ($v in $volumes) {
    $pct = [math]::Round(($v.SizeRemaining / $v.Size) * 100, 1)
    $report.warnings += "DISK SPACE: Drive $($v.DriveLetter): only $([math]::Round($v.SizeRemaining/1GB, 1))GB free ($pct%)"
}

# Check for critical/error events in last hour (excluding known noise)
$criticals = Get-WinEvent -FilterHashtable @{LogName='System'; Level=1,2; StartTime=(Get-Date).AddHours(-1)} -ErrorAction SilentlyContinue |
    Where-Object { $_.ProviderName -notmatch 'DistributedCOM|Service Control Manager' }
if ($criticals.Count -gt 5) {
    $report.warnings += "EVENTS: $($criticals.Count) critical/error events in last hour"
}

# Check uptime
$uptime = (Get-Date) - (Get-CimInstance Win32_OperatingSystem).LastBootUpTime
$report.stats.uptimeHours = [math]::Round($uptime.TotalHours, 1)

# Build temp string
$tempStr = ""
if ($report.stats.cpuTemp) { $tempStr += "CPU:$($report.stats.cpuTemp)C " }
if ($report.stats.gpuTemp) { $tempStr += "GPU:$($report.stats.gpuTemp)C " }
if ($report.stats.gpuHotspot) { $tempStr += "Hotspot:$($report.stats.gpuHotspot)C" }

# Output
if ($report.issues.Count -eq 0 -and $report.warnings.Count -eq 0) {
    Write-Output "HEALTH_OK | Uptime: $($report.stats.uptimeHours)h | $tempStr"
} else {
    Write-Output "HEALTH_ALERT"
    Write-Output "Timestamp: $($report.timestamp)"
    Write-Output "Uptime: $($report.stats.uptimeHours) hours"
    if ($tempStr) { Write-Output "Temps: $tempStr" }
    if ($report.issues) {
        Write-Output "`n=== ISSUES ==="
        $report.issues | ForEach-Object { Write-Output "  ! $_" }
    }
    if ($report.warnings) {
        Write-Output "`n=== WARNINGS ==="
        $report.warnings | ForEach-Object { Write-Output "  * $_" }
    }
}
