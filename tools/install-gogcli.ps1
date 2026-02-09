$url = "https://github.com/steipete/gogcli/releases/download/v0.9.0/gogcli_0.9.0_windows_amd64.zip"
$zip = "$env:TEMP\gogcli.zip"
$dest = "C:\Users\Grant\AppData\Local\Programs\gogcli"

Write-Host "Downloading gogcli v0.9.0..."
Invoke-WebRequest -Uri $url -OutFile $zip

Write-Host "Extracting to $dest..."
New-Item -ItemType Directory -Force -Path $dest | Out-Null
Expand-Archive -Path $zip -DestinationPath $dest -Force
Remove-Item $zip

# Add to PATH for current user
$userPath = [Environment]::GetEnvironmentVariable("PATH", "User")
if ($userPath -notlike "*$dest*") {
    [Environment]::SetEnvironmentVariable("PATH", "$userPath;$dest", "User")
    Write-Host "Added to PATH. Restart terminal for changes."
}

Write-Host "Done! Run 'gog --version' in a new terminal."
