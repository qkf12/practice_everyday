@echo off
chcp 65001 >nul
title 明日香桌宠
echo ========================================
echo    明日香桌宠启动中...
echo ========================================
echo.

cd /d "%~dp0"

set "PYTHONW="

REM 1. 优先使用项目目录下的 runtime (如果存在)
if exist "%~dp0runtime\python\pythonw.exe" (
    set "PYTHONW=%~dp0runtime\python\pythonw.exe"
    goto :launch
)

REM 2. 查找豆包沙箱运行时 Python
for /d %%D in ("%LOCALAPPDATA%\Doubao\User Data\sandbox_runtime\bases\*") do (
    if exist "%%D\python\pythonw.exe" (
        set "PYTHONW=%%D\python\pythonw.exe"
        goto :launch
    )
)

REM 3. 查找豆包沙箱 envs Python
for /d %%D in ("%LOCALAPPDATA%\Doubao\User Data\Default\sandbox_envs_dir\envs\*") do (
    if exist "%%D\python\pythonw.exe" (
        set "PYTHONW=%%D\python\pythonw.exe"
        goto :launch
    )
)

REM 4. 使用系统 PATH 中的 pythonw
where pythonw >nul 2>&1
if %errorlevel%==0 (
    set "PYTHONW=pythonw"
    goto :launch
)

echo [错误] 未找到可用的 Python 环境！
echo.
echo 请确保已安装 Python 并添加到 PATH，
echo 或将 Python 运行时复制到本目录下的 runtime\python\ 文件夹。
echo.
pause
exit /b 1

:launch
echo 使用 Python: %PYTHONW%
start "" "%PYTHONW%" main.py

echo.
echo 桌宠已启动！
echo 提示: 左键点击明日香打开工具箱，右键调节大小或退出。
timeout /t 2 >nul
exit
