@echo off
chcp 65001 >nul
title 明日香桌宠
echo ========================================
echo    明日香桌宠启动中...
echo ========================================
echo.

set "PYTHON=C:\Users\32738\AppData\Local\Doubao\User Data\Default\sandbox_envs_dir\envs\12a5371e-b995-4c6a-b980-8576d71cb340\python\pythonw.exe"

if not exist "%PYTHON%" (
    echo [错误] 未找到 Python 环境，尝试使用系统 python...
    set "PYTHON=pythonw"
)

cd /d "%~dp0"
start "" "%PYTHON%" main.py

echo 桌宠已启动！
echo 提示: 左键点击明日香打开工具箱，右键打开菜单，拖拽可移动位置。
timeout /t 3 >nul
exit
