echo "新建虚拟环境"
python -m venv venv
source venv/bin/activate
echo "环境初始化"
pip install -r requirements.txt
echo "环境初始化完成"

echo "WD14-Tagger 安装依赖"
cd custom_nodes/ComfyUI-WD14-Tagger
pip install -r requirements.txt
cd ..
cd ..
