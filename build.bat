@echo off
title CYPY Build
echo ========================================
echo   CYPY Build Script
echo ========================================
echo.

REM Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Python not found. Please install Python 3.8+ first.
    pause
    exit /b 1
)

echo [i] Running build...
echo.
python build.py

if %errorlevel% neq 0 (
    echo.
    echo [!] Build failed.
    pause
    exit /b 1
)

echo.
echo ========================================
echo   Build completed! Check releases/ folder
echo ========================================
pause
