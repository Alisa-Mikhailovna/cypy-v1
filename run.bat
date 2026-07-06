@echo off
title CYPY - Cyrene's Python Manga Translator
echo ========================================
echo   Starting CYPY...
echo ========================================
echo.

REM Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Python not found. Please install Python 3.8+ first.
    pause
    exit /b 1
)

REM Check if .env exists
if not exist .env (
    echo [i] No .env found. Copying from .env.example...
    if exist .env.example (
        copy .env.example .env >nul
        echo [+] .env created. Please edit it with your API key.
        notepad .env
    ) else (
        echo [!] No .env.example found. Please create .env manually.
    )
)

REM Run the app
python -m cypy

if %errorlevel% neq 0 (
    echo.
    echo [!] CYPY exited with error.
    pause
)
