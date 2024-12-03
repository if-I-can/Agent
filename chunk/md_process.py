import os

# 输入原目录和输出目录
source_dir = '/home/zsl/Agent/test_markdown1'
output_dir = '/home/zsl/Agent/PDF/processed_paper_md'  # 新目录

# 创建输出目录，如果不存在
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 处理单个文件
def process_md_file(file_path, output_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # 删除所有包含#的行，去除所有的*和$$字符，并避免多个连续的空行
    processed_lines = []
    prev_line_empty = False  # 标记上一行是否为空行
    
    for line in lines:
        if not line.startswith('#') and not line.startswith('!') and not line.startswith('---') and not line.startswith('&'):
            if len(line.strip()) < 50:  # 如果去除空格后的行长度小于4
                continue
            # 去除所有的*和$$字符
            line = line.replace('*', '').replace('$$', '')
            
            # 如果当前行是空行，检查是否是连续的空行
            if line.strip() == '':  # 如果是空行
                if prev_line_empty:  # 如果前一行已经是空行，则跳过当前空行
                    continue
                prev_line_empty = True  # 设置标记为空行
            else:
                prev_line_empty = False  # 当前行不是空行，清除标记
                
            # 添加当前行到结果
            processed_lines.append(line)
    
    # 保存处理后的内容到新文件
    with open(output_path, 'w', encoding='utf-8') as file:
        file.writelines(processed_lines)

# 遍历源目录中的所有Markdown文件
for filename in os.listdir(source_dir):
    if filename.endswith('.md'):
        file_path = os.path.join(source_dir, filename)
        output_path = os.path.join(output_dir, filename)
        
        # 处理文件
        process_md_file(file_path, output_path)

print("处理完毕，文件已保存到新目录：", output_dir)
