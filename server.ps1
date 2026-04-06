# Portfolio Local Dev Server
# Run this script to start a local server for the portfolio

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Starting Portfolio Dev Server..." -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if npx is available
if (Get-Command npx -ErrorAction SilentlyContinue) {
    Write-Host "Starting server at http://localhost:3000" -ForegroundColor Green
    Write-Host "Press Ctrl+C to stop" -ForegroundColor Yellow
    Write-Host ""
    npx -y serve .
}
else {
    Write-Host "npx not found. Opening index.html directly..." -ForegroundColor Yellow
    Start-Process "index.html"
}
