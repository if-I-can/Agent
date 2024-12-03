import os
from chonkie import SemanticChunker

def merge_table_chunks(chunks):
    """
    合并跨块的 Markdown 表格。
    如果一个块的最后一行以 '|' 结尾，且下一个块的第一行以 '|' 开头，则合并它们。
    """
    merged_chunks = []
    buffer = []  # 用于存储当前待合并的块

    for chunk in chunks:
        lines = chunk.text.splitlines()  # 将当前块按行分割
        if buffer:
            # 如果当前缓冲区非空，检查是否需要合并
            if lines and lines[0].strip().startswith("|"):
                buffer.append(chunk.text)  # 合并当前块内容到缓冲区
            else:
                # 如果不需要合并，将缓冲区合并为一个块
                merged_chunks.append("\n".join(buffer))
                buffer = [chunk.text]  # 启动新的缓冲区
        else:
            buffer = [chunk.text]  # 启动新的缓冲区
    
    # 处理最后的缓冲区
    if buffer:
        merged_chunks.append("\n".join(buffer))

    return merged_chunks


# 初始化分块器
chunker = SemanticChunker(
    embedding_model="minishlab/potion-base-8M",  # 使用的模型
    similarity_threshold=0.9,                   # 相似性阈值
    chunk_size=2056,                            # 每个块的最大字数
    min_chunk_size=20,                          # 最小块大小
    initial_sentences=10,                       # 初始分块包含的句子数量
)

input_folder = '/home/zsl/Agent/PDF/processed_paper_md'  # 源文件夹路径
output_folder = '/home/zsl/Agent/PDF/result'            # 目标文件夹路径

# 遍历所有 Markdown 文件
md_files = [f for f in os.listdir(input_folder) if f.endswith('.md')]

for md_file in md_files:
    input_path = os.path.join(input_folder, md_file)
    # 使用文件名（去掉扩展名）创建单独文件夹
    folder_name = os.path.splitext(md_file)[0]
    folder_path = os.path.join(output_folder, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    
    # 读取 Markdown 文件内容
    with open(input_path, 'r', encoding='utf-8') as file:
        md_content = file.read()

    # 对文本进行分块
    chunks = chunker(md_content)
    # 合并跨块的表格
    merged_chunks = merge_table_chunks(chunks)

    # 保存合并后的块到单独的 Markdown 文件
    for i, chunk in enumerate(merged_chunks):
        chunk_file_name = f"chunk_{i + 1}.md"
        output_path = os.path.join(folder_path, chunk_file_name)
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(chunk + '\n\n')  # 在每个块后添加空行
        print(f"Processed chunk {i + 1} of {md_file}, saved to {output_path}")

    print(f"Processed: {md_file}")
