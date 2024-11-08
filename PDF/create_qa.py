from openai import OpenAI
import json
import os 
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, Back, Style, init
folder_path = os.getenv("FOLDER_PATH", "/home/zsl/Agent/PDF/paper_md")
output_file = "/home/zsl/Agent/PDF/qa.json"
output_tep = []



def format_final_answer(final_answer):
    # 使用正则表达式匹配每个问题，包括最后一个问题
    pattern = r"(\d+)\.\s+\*\*(.*?)\*\*\s*([^\d]+?)(?=\n\d+\.|\Z)"
    questions = []

    # 使用 re.findall 查找所有匹配的内容
    matches = re.findall(pattern, final_answer, re.DOTALL)
    
    for match in matches:
        question_text = f"**{match[1].strip()}** {match[2].strip()}"  # 重构问题内容
        questions.append(question_text)

    return questions





def clean_json_string(json_string):
    try:
        # Remove triple backticks and "json" tag if present
        json_string = re.sub(
            r"^```json\s*|\s*```$", "", json_string, flags=re.MULTILINE
        )

        # Remove any leading/trailing whitespace
        json_string = json_string.strip()

        # Try to parse the JSON as is
        json.loads(json_string)
        return json_string
    
    except json.JSONDecodeError:
        # If parsing fails, try to fix common issues

        # Replace any non-standard quotes with standard double quotes
        json_string = re.sub(r"[" "]", '"', json_string)

        # Ensure property names are in double quotes
        json_string = re.sub(r"(\w+)(?=\s*:)", r'"\1"', json_string)

        # Replace single quotes with double quotes, but not within text
        json_string = re.sub(r"(?<!\\)'", '"', json_string)

        return json_string


def escape_filename(filename):
    try:
        # Replace problematic characters with underscores
        escaped = re.sub(r"[^\w\-_\. ]", "_", filename)
        # Replace spaces with underscores
        escaped = escaped.replace(" ", "_")
        return escaped
    except Exception as e:
        print(f"Error escaping filename {filename}: {e}")
        return filename
    

class QAagent():
    def __init__(self, model="deepseek-chat"):
        self.clint = OpenAI(base_url=os.getenv("OPENAI_API_BASE"), api_key=os.getenv("OPENAI_API_KEY"))
        self.model = model
    
    def generate_q(self, prompt_q) -> str:
        response = self.clint.chat.completions.create(messages=prompt_q, model=self.model)
        return str(response.choices[0].message.content)
    
    def reflect_q(self, prompt_f) -> str:
        
        response = self.clint.chat.completions.create(messages=prompt_f, model=self.model)
        return str(response.choices[0].message.content)


agent = QAagent()

chat_historty = []

def process_file(filename):
    # 这里使用局部变量 output_results 存储当前文件处理结果
    output_results = []
    try:
        print(f"处理文件: {filename}")
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            md_content = file.read()

        # 第一阶段：生成复杂问题
        PROMPT_Q = [
            {
                "role": "system",
                "content": "你是一位专业的渔业知识评估助手，负责根据提供的渔业相关文章生成深入的专业问题。如果用户针对你的问题给出修改建议，那你需要按照建议修改你提出的问题"
            },
            {
                "role": "user",
                "content": f"""
请根据以下渔业相关内容生成5个复杂的专业问题。要求如下:
1. 问题应围绕核心技术与原理提出，要求具有深度和广度。
2. 问题应避免使用"基于这篇文章"、"如何根据本实验结果"、"在本文提出的"等表述。
3. 确保问题表述专业、清晰，能够引发深入讨论。
以下是需要分析的渔业相关内容:
{md_content}
请生成5个符合上述要求的复杂专业问题。
                """
            },
        ]
        
        # 获取第一个 Agent 的问题
        questions = agent.generate_q(PROMPT_Q)
        print(Fore.LIGHTGREEN_EX,questions)
        # print("生成的初始问题:", questions)
        # 第二阶段：让第二个 Agent 评估并提供反馈

        PROMPT_F = [
            {
                "role": "system",
                "content": f"""以下是第一个模型根据{md_content}生成的渔业相关专业问题。请对每个问题进行审查，具体审查角度如下：
1. 检查问题的清晰度：问题是否表述清晰，易于理解？如果有模糊之处，请指出并给出改进建议。
3. 分析问题的可讨论性：问题是否能够引发技术专家之间的深入讨论？如果问题过于简单或过于复杂，提供平衡的建议。
4. 评估问题的广度与深度：问题是否能够覆盖渔业领域中的核心技术和原理？是否避免了过于狭窄或过于广泛的提问？
请根据以下问题逐一分析和提供反馈：
{questions}
只需要提供你对每个问题最终的修改建议或优化方向，帮助提高其质量，而审查过程不用阐述"""
            }
        ]
        
        # 获取第二个 Agent 的反馈
        feedback = agent.reflect_q(PROMPT_F)
        print(Fore.BLUE,feedback)
        # print("第二个 Agent 的反馈:", feedback)

        # 第三阶段：根据反馈修改问题，要求生成修改后的问题
        PROMPT_Q_MODIFIED = [
            {
                "role": "system",
                "content": "请根据以下反馈优化生成的问题。"
            },
            {
                "role": "user",
                "content": f"""
以下是反馈建议，请根据这些建议重新对你生成的5个问题进行优化：

反馈建议：
{feedback}

请根据这些修改建议，生成优化后的问题。每个问题都应该按照反馈建议进行一定优化：
                """
            },
        ]
        
        # 获取修改后的问题
        final_questions = agent.generate_q(PROMPT_Q_MODIFIED)
        print(Fore.CYAN,final_questions)
        format_final_questions = format_final_answer(final_questions)
        escaped_filename = escape_filename(filename)
        print(Fore.GREEN,format_final_questions)
        print(len(format_final_questions))
        for question in format_final_questions:
            PROMPT_A=[
                {
                    "role": "system",
                    "content": """你是一位渔业和水产养殖领域的顶级专家，尤其精通鱼类养殖、智能投喂系统、水质管理和相关技术创新。你的职责是提供最专业、最前沿、最准确的答案，并从给定内容中识别和提取最相关的关键段落。""",
                },
                {
                    "role": "user",
                    "content": f"""
请根据以下问题和相关内容，提供一个高度专业、准确且详尽的回答，并识别最相关的关键段落。你的任务分为两个部分：

第一部分：提供专业回答
1. 展现深厚的学术背景和实践经验，运用专业术语和概念。
2. 提供具体的数据支持，包括相关统计数据、研究结果或行业标准。
3. 引用最新的研究成果和技术进展，体现对行业前沿的把握。
4. 分析问题的多个方面，考虑不同的影响因素和潜在的挑战。
5. 提供实际案例或应用场景，说明理论如何在实践中应用。
6. 讨论相关技术或方法的优缺点，以及未来可能的发展方向。
7. 如果适用，提及环境影响、可持续性考虑或经济效益分析。
8. 直接引用论文中的具体数据、实验结果或统计信息,并明确标注出处。
9. 使用论文中提到的专业术语和概念,并简要解释其含义。
10. 详细讨论论文中提出的主要观点、方法或技术,分析其创新性和实际应用价值。

第二部分：识别关键段落
1. 仔细审视给定的内容，找出与问题最相关的段落。
2. 选择至少3个关键段落，每个段落应至少包含200字。
3. 确保选择的段落直接支持或补充你的专业回答。
4. 对于每个选定的段落，提供原文和准确的中文译文（如果原文是英文）。
5. 选择的关键段落应包含具体的数据、实验结果或重要结论。
6. 解释每个关键段落与问题的相关性,以及如何支持你的专业回答。

问题：{question}
相关内容：
{md_content}

请生成一个JSON对象，包含以下字段：
- 问题：使用给定的问题
- 最佳答案：按照上述第一部分要求提供的详细专业回答，长度不少于300字
- 参考来源："{os.path.splitext(escaped_filename)[0]}.pdf"
- 关键段落：按照第二部分要求选择的至少3个关键段落，每个包含{{"原文": "","中文译文": ""}}

请确保你的回答紧密结合论文内容,大量引用论文中的具体数据、方法和结论。避免泛泛而谈,而应深入分析论文的核心观点和创新之处。你的回答应体现出高度的专业性和准确性，同时关键段落应与问题和你的回答高度相关，为你的论点提供直接支持。
                """,
                },
            ]
            answer = agent.generate_q(PROMPT_A)
            cleaned_json = clean_json_string(answer)
            json_data = json.loads(cleaned_json)
            json_data["version"] = "1.1-dev"
            json_data["参考来源"] = [f"{os.path.splitext(escaped_filename)[0]}.pdf"]
            if json_data:
                output_results.append(json_data)  # 将当前问题的处理结果添加到局部变量里
                print(f"成功生成题目 ({filename}): {question[:50]}...")
        return output_results  # 返回局部变量中的结果
    except Exception as e:
        print(f"Error processing file {filename}: {e}")
        return []


# 使用多线程处理文件
try:
    with ThreadPoolExecutor(max_workers=1) as executor:
        futures = [
            executor.submit(process_file, filename)
            for filename in os.listdir(folder_path)
            if filename.endswith(".md")
        ]
        for future in as_completed(futures):
            result = future.result()
            if result:
                output_tep.extend(result)  # 将每个文件的结果添加到全局变量 output_tep

    # 将结果写入文件
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(output_tep, file, ensure_ascii=False, indent=4)

    print(f"数据已成功写入 {output_file}")
except Exception as e:
    print(f"Error during the main execution: {e}")

