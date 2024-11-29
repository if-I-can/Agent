import spacy
import os
import re
import numpy as np

# 加载 spaCy 更高精度模型
nlp = spacy.load("en_core_web_lg")  # 使用 "en_core_web_lg" 进行更高精度的相似度计算

def clean_and_merge_text(text):
    # 移除所有非字母、数字、换行符的字符
    text = re.sub(r'[^\w\s\n]', '', text)  # 保留字母、数字、空格和换行符
    # 移除类似 "%C", "JL" 和特殊字符（如 'ü'）
    text = re.sub(r'[%\w]*C|JL|ü|[^\x00-\x7F]+', '', text)  # 清理特殊字符
    # 移除类似DNA序列（连续字母和数字，长度较长）
    text = re.sub(r'[ACGTacgt0-9]{5,}', '', text)  # 例如 DNA 或误识别的序列
    # 去除所有形式的图表、文献引用等
    text = re.sub(r'Fig\s*\d+|accession\s*No\s*\S+', '', text)  # 去除图表和文献编号
    text = re.sub(r'\n+', ' ', text)  # 合并多余的换行符
    text = re.sub(r'(\w)-(\w)', r'\1\2', text)  # 合并被拆分的单词
    # 清理多余的空格
    text = re.sub(r'\s+', ' ', text)  # 将多余的空格替换成一个空格
    text = text.strip()  # 去除首尾的空格
    return text

# 读取 Markdown 文件内容并将其转换为纯文本
def read_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # 去除 Markdown 语法标记
    text = re.sub(r'#.*', '', text)  # 去除标题（#）
    text = re.sub(r'\*.*\*', '', text)  # 去除斜体标记（*）
    text = re.sub(r'!\[.*\]\(.*\)', '', text)  # 去除图片标记
    text = re.sub(r'\[.*\]\(.*\)', '', text)  # 去除链接标记
    text = re.sub(r'\n+', ' ', text)  # 合并多余的换行符
    text = re.sub(r'(\w)-(\w)', r'\1\2', text)  # 合并被拆分的单词

    # 删除连续的数字（例如：3 556 9 9 12 3 3333 等）
    text = re.sub(r'\d{2,}\s*\d{2,}', '', text)  # 删除多于2个数字之间有空格的模式（数字序列）

    # 删除单个数字
    text = re.sub(r'\b\d{1,3}\b', '', text)  # 删除单个数字，最多三位数字

    # 进一步清理文本
    text = clean_and_merge_text(text)
    
    # 打印清理后的文本

    
    return text  # 返回提取的文本

# 计算段落相似度（通过词向量池化）
def get_paragraph_similarity(query, doc_text):
    query_doc = nlp(query)  # 查询问题的 spaCy 文档
    doc = nlp(doc_text)  # 要比较的段落文本

    # 获取每个词的词向量，计算平均词向量作为段落的向量表示
    vectors1 = [token.vector for token in query_doc if token.has_vector]
    vectors2 = [token.vector for token in doc if token.has_vector]

    # 检查是否有有效的词向量
    if len(vectors1) == 0 or len(vectors2) == 0:
        return 0.0  # 如果没有有效词向量，直接返回相似度为 0

    # 计算平均词向量
    vector1 = np.mean(vectors1, axis=0)
    vector2 = np.mean(vectors2, axis=0)

    # 计算余弦相似度
    cosine_similarity = np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))

    return float(cosine_similarity)  # 确保返回的是标量
# 从文件中提取段落并计算与问题的相似度
def find_most_similar_paragraphs(query, file_path, top_n=3):
    doc_text = read_md_file(file_path)  # 获取 Markdown 文件中的文本
    doc = nlp(doc_text)
    similarities = []
    for sent in doc.sents:
        similarity = get_paragraph_similarity(query, sent.text)
        similarities.append((sent.text, similarity))

    similarities.sort(key=lambda x: x[1], reverse=True)

    return [paragraph for paragraph, _ in similarities[:top_n]]

# 遍历文件夹并查询每个 Markdown 文件
def search_in_folder(query, folder_path, top_n=1):
    similar_paragraphs_per_file = {}
    # 遍历文件夹中的所有 .md 文件
    for filename in os.listdir(folder_path):
        if filename.endswith(".md"):  # 只处理 Markdown 文件
            file_path = os.path.join(folder_path, filename)
            similar_paragraphs = find_most_similar_paragraphs(query, file_path, top_n)
            similar_paragraphs_per_file[filename] = similar_paragraphs
    
    return similar_paragraphs_per_file

# 示例使用
query = "Results of Counting Trials"
folder_path = '/home/zsl/Agent/PDF/paper_md'  # 存放 Markdown 文件的文件夹路径
# 获取每个文件中最相似的段落
similar_paragraphs_per_file = search_in_folder(query, folder_path, top_n=3) 

all_similar_paragraphs = []
for file_name, paragraphs in similar_paragraphs_per_file.items():
    for paragraph in paragraphs:
        if len(paragraph) > 150:  # 可以调整长度过滤条件
            all_similar_paragraphs.append((file_name, paragraph))
        else:
            continue

# 打印所有相似段落并进行格式化输出
print(f"Found {len(all_similar_paragraphs)} paragraphs with the query: '{query}'\n")
for idx, (file_name, paragraph) in enumerate(all_similar_paragraphs, start=1):
    print(f"--- {file_name} --- Paragraph {idx} ---")
    print(paragraph)
    print("\n" + "-"*50 + "\n")
