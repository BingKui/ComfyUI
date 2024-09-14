#!/bin/bash

echo "进入虚拟环境"

folder_path="venv"

# 使用 [ -d ] 测试操作符检查文件夹是否存在
if [ -d "$folder_path" ]; then
    echo "文件夹存在：$folder_path"
    source venv/bin/activate
    python main.py
else
    echo "虚拟环境不存在，请先执行 udotai_init.sh 初始化"
    exit 1
fi