"""
大模型下载脚本
"""
model_download.py
import os
import torch
from modelscope import snapshot_download, AutoModel, AutoTokenizer
model_dir = snapshot_download('qwen/Qwen2-7B-Instruct', cache_dir='/home/zsl/home', revision='master')


# 大模型地址： 



