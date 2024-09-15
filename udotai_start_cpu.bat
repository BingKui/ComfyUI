@echo off
chcp 65001

echo 进入虚拟环境

set folder_path=venv

REM 使用 IF 语句检查文件夹是否存在
IF EXIST "%folder_path%\" (
    echo 文件夹存在：%folder_path%
    call venv\Scripts\activate
    echo 使用CPU模式启动
    python main.py --cpu
) ELSE (
    echo 虚拟环境不存在，请先执行 udotai_init.bat 初始化
    exit /b 1
)