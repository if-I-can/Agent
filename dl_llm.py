# model_download.py
import os
import torch
from modelscope import snapshot_download, AutoModel, AutoTokenizer
model_dir = snapshot_download('intfloat/e5-mistral-7b-instruct', cache_dir='/home/zsl/Agent', revision='master')


# 大模型地址： 
# /home/zsl/home/hub/qwen/Qwen2-7B-Instruct



