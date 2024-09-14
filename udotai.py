import os
import requests

# def download_file(download_url, file_name, folder_path):
#     """
#     下载文件并保存到指定目录，文件名为指定名称。

#     :param download_url: 文件的下载链接
#     :param file_name: 下载后的文件名
#     :param folder_path: 文件保存的目录路径
#     """
#     # 确保保存目录存在
#     if not os.path.exists(folder_path):
#         os.makedirs(folder_path)

#     # 完整的文件保存路径
#     save_path = os.path.join(folder_path, file_name)

#     # 发起请求下载文件
#     with requests.get(download_url, stream=True) as r:
#         r.raise_for_status()  # 确保请求成功
#         with open(save_path, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=8192):
#                 f.write(chunk)

#     print(f"文件已下载并保存到：{save_path}")

def download_file(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"文件已下载至：{filename}")
    else:
        print("文件下载失败")

# 执行下载模型文件
base_path = os.path.dirname(os.path.realpath(__file__))
models_dir = os.path.join(base_path, "models")
custom_nodes_directory = os.path.join(base_path, "custom_nodes")


# 下载 ComfyUI WD 1.4 Tagger 所需的模型文件
wd_tagger_model_url = "https://hf-mirror.com/SmilingWolf/wd-v1-4-convnextv2-tagger-v2/blob/main/model.onnx"
wd_tagger_model_path = os.path.join(custom_nodes_directory, 'ComfyUI-WD14-Tagger/models')
wd_tagger_model_name = os.path.join(wd_tagger_model_path, "wd-v1-4-convnextv2-tagger-v2.onnx")
download_file(wd_tagger_model_url, wd_tagger_model_name)
# 下载 ComfyUI WD 1.4 Tagger 所需的csv文件
wd_tagger_csv_url = "https://hf-mirror.com/SmilingWolf/wd-v1-4-convnextv2-tagger-v2/blob/main/selected_tags.csv"
wd_tagger_csv_name = os.path.join(wd_tagger_model_path, "wd-v1-4-convnextv2-tagger-v2.cvs")
download_file(wd_tagger_csv_url, wd_tagger_csv_name)


# download_file("https://huggingface.co/ljy-ai/udotai/resolve/main/udotai.py", "udotai.py", custom_nodes_directory)