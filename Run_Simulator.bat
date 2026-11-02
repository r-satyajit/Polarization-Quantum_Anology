@echo off
cd /d "%~dp0"
python --version >nul 2>&1
if %errorlevel% equ 0 (
    pip install -r requirements.txt
    python quantum_polarization.py
) else (
    start "" "%~dp0polarization.html"
)
