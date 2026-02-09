# Gmail inbox checker for OpenClaw
# Checks for unread emails and outputs summary

$account = "redrum137@gmail.com"
$maxResults = 5

try {
    $result = gog gmail search "is:unread -category:promotions -category:social" --account $account --max $maxResults --json 2>&1
    
    if ($LASTEXITCODE -ne 0) {
        Write-Output "GMAIL_ERROR: Failed to fetch emails - $result"
        exit 1
    }
    
    $data = $result | ConvertFrom-Json
    
    if ($data.threads -and $data.threads.Count -gt 0) {
        Write-Output "GMAIL_ALERT: $($data.threads.Count) unread email(s) in Primary inbox"
        foreach ($thread in $data.threads) {
            Write-Output "- From: $($thread.from)"
            Write-Output "  Subject: $($thread.subject)"
            Write-Output "  Date: $($thread.date)"
            Write-Output ""
        }
    } else {
        Write-Output "GMAIL_OK"
    }
} catch {
    Write-Output "GMAIL_ERROR: $($_.Exception.Message)"
    exit 1
}
