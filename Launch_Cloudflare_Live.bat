@echo off
title ClearDrive AI - Live Cloudflare Edge Launcher
color 0b
echo =====================================================================
echo       CLEAR-DRIVE AI : NEXT-GEN PREDICTIVE V2X COCKPIT
echo               LIVE CLOUDFLARE EDGE LAUNCHER
echo =====================================================================
echo.
echo [+] Starting ClearDrive AI Python Engine on Port 5000...
start /b python -u app.py
timeout /t 3 /nobreak >nul
echo [+] Connecting Cloudflare Edge Tunnel & Syncing Worker...
echo.
python launch_live_tunnel.py
pause
