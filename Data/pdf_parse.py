import os
import pdfplumber

def pdf_to_markdown(pdf_path: str, output_md_path: str):
    # 打开 PDF 文件
    with pdfplumber.open(pdf_path) as pdf:
        # 初始化 Markdown 内容
        markdown_content = ""
        
        for page in pdf.pages:
            # 添加页码作为标题
            markdown_content += f"# Page {page.page_number}\n\n"
            
            # 提取文本内容
            text_content = page.extract_text()
            if text_content:
                # 将文本内容添加到 Markdown 内容中
                markdown_content += text_content + "\n\n"
            else:
                markdown_content += "此页没有可提取的文本。\n\n"

    # 保存为 Markdown 文件
    with open(output_md_path, 'w', encoding='utf-8') as md_file:
        md_file.write(markdown_content)

def process_pdf_folder(folder_path: str, output_base_dir: str):
    """
    处理指定文件夹下所有 PDF 文件并保存为 Markdown 文件。
    """
    if not os.path.exists(output_base_dir):
        os.makedirs(output_base_dir)  # 创建输出目录

    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)
            md_filename = os.path.splitext(filename)[0] + '.md'  # 创建 Markdown 文件名
            output_md_path = os.path.join(output_base_dir, md_filename)

            print(f"Processing PDF file: {pdf_path}")
            pdf_to_markdown(pdf_path, output_md_path)

if __name__ == "__main__":
    # 示例使用
    input_folder_path = r'/home/zsl/Agent/Data/pdf'  # PDF 文件所在的文件夹
    output_folder_path = r'/home/zsl/Agent/Data/pdf_md'  # 输出 Markdown 文件的文件夹
    process_pdf_folder(input_folder_path, output_folder_path)
