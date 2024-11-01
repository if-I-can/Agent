#!/bin/bash

# 检查是否提供了所需的参数
if [ "$#" -ne 2 ]; then
    echo "用法: $0 <输入文件夹> <输出文件夹>"
    exit 1
fi

# 赋值输入和输出文件夹
input_folder="$1"
output_folder="$2"

# 检查输入文件夹是否存在
if [ ! -d "$input_folder" ]; then
    echo "错误: 输入文件夹不存在。"
    exit 1
fi

# 如果输出文件夹不存在，则创建它
mkdir -p "$output_folder"

# 处理输入文件夹中的每个PDF文件
for pdf_file in "$input_folder"/*.pdf; do
    # 检查是否有PDF文件
    if [ ! -e "$pdf_file" ]; then
        echo "在输入文件夹中没有找到PDF文件。"
        exit 1
    fi

    # 获取不带路径和扩展名的文件名
    filename=$(basename -- "$pdf_file")
    filename_no_ext="${filename%.*}"

    # 在输出文件夹中为每个PDF创建一个子文件夹
    pdf_output_folder="$output_folder/$filename_no_ext"
    mkdir -p "$pdf_output_folder"

    echo "正在处理: $filename"

    # 调用Python脚本处理PDF
    python3 pdf_parser.py "$pdf_file" "$pdf_output_folder"

    echo "完成处理: $filename"
    echo "----------------------------------------"
done

echo "所有PDF文件已处理完毕。"