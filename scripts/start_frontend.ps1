# PowerwallDashboard - Start Frontend Static Server (Windows PowerShell)
# Usage:
#   pwsh -File .\scripts\start_frontend.ps1

$ErrorActionPreference = "Stop"

$Base = "C:\Users\madgu\tesla-project\PowerwallDashboard"
$Python = Join-Path $Base ".venv\Scripts\python.exe"

Write-Host "Serving index.html from $Base at http://127.0.0.1:5500" -ForegroundColor Cyan

& $Python -m http.server 5500 --directory $Base