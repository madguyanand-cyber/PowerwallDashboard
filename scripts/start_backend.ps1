# PowerwallDashboard - Start Backend (Windows PowerShell)
# Usage: Right-click this file and run with PowerShell, or execute in terminal:
#   pwsh -File .\scripts\start_backend.ps1

$ErrorActionPreference = "Stop"

# Paths
$Base = "C:\Users\madgu\tesla-project\PowerwallDashboard"
$Python = Join-Path $Base ".venv\Scripts\python.exe"

# Configuration
# Non-secret identifier for TeslaPy login. Update if you prefer a different email.
$env:TESLA_EMAIL = "madguyanand@gmail.com"

Write-Host "Starting backend with TESLA_EMAIL=$($env:TESLA_EMAIL)" -ForegroundColor Cyan

# Run the app. On first run, it will print an authorization URL; open it, complete login,
# and paste the final blank-page URL back into the terminal when prompted.
& $Python (Join-Path $Base "app.py")