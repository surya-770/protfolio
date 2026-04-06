$filePath = "c:\Users\rayis\OneDrive\Desktop\ai\portfolio\js\app.js"
$lines = Get-Content $filePath
$targetPattern = "const certIcons = {"

$targetIndex = -1
for ($i = 0; $i -lt $lines.Length; $i++) {
    if ($lines[$i] -match $targetPattern) {
        $targetIndex = $i
        break
    }
}

if ($targetIndex -ne -1) {
    $newLines = $lines[0..($targetIndex - 1)]
    $newLines | Set-Content $filePath
    Write-Host "File successfully truncated before certIcons."
} else {
    Write-Host "Target not found."
}
