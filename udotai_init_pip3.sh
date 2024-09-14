echo "新建虚拟环境"
python3 -m venv venv
source venv/bin/activate
echo "环境初始化"
pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
echo "环境初始化完成"

echo "WD14-Tagger 安装依赖"
cd custom_nodes/ComfyUI-WD14-Tagger
pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
cd ..
cd ..




