import json
import os
import re
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferWindowMemory
from langchain.agents import LLMSingleActionAgent, AgentExecutor
from custom_parser import CustomOutputParser, CustomPromptTemplate
from select_tools import tools, tool_names
from callbacks import CustomAsyncIteratorCallbackHandler
from flask import Flask, request, jsonify, render_template

# 从 _prompt.txt 读取 system_prompt
with open("/home/zsl/Agent/Data/prompt.txt", "r") as f:
    system_prompt = f.read()

# 解析 system_prompt 文档
prompt_template_agent = CustomPromptTemplate(
    template=system_prompt,
    tools=tools,
    input_variables=["input", "intermediate_steps", "history"],
)

# 根据用户输入得到规划
callback = CustomAsyncIteratorCallbackHandler()

# 生成答案的模型需求
model = ChatOpenAI(
    model_name="deepseek-chat",  # Replace with the correct DeepSeek model name
    verbose=True,
    callbacks=[callback],
    temperature=0.0,
    openai_api_base="https://api.deepseek.com",  # 直接设置 DeepSeek API 基础 URL
    openai_api_key="sk-027ac6afb5bc4cfb8ccb0b51fc3c5b26",  # 直接设置 DeepSeek API 密钥
)

llm_chain = LLMChain(llm=model, prompt=prompt_template_agent)
output_parser = CustomOutputParser()

# 创建代理
agent = LLMSingleActionAgent(
    llm_chain=llm_chain,
    output_parser=output_parser,
    stop=["\nObservation:", "Observation"],
    allowed_tools=tool_names,
)

# 初始化记忆
memory = ConversationBufferWindowMemory(k=0)

# 创建代理执行器
agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent,
    tools=tools,
    verbose=True,
    memory=memory,
)

app = Flask(__name__)

# Flask route for rendering the frontend
@app.route('/')
def home():
    return render_template('index.html')

# Flask route for handling the API request
@app.route('/api/agent', methods=['POST'])
def invoke_agent():
    user_input = request.json.get('input')

    # 确保输入是有效的
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    # 调用 agent_executor 获取响应
    try:
        # 假设 agent_executor 是一个已经初始化并可以调用的对象
        response = agent_executor.invoke({"input": user_input})
        # print("resonse is:",response)
        response_out = response.get("output", "")

        # 使用正则表达式提取"主要内容"和"结论"
        conclusion_match1 = re.search(r"主要内容：\s*(.+)", response_out)
        conclusion_match2 = re.search(r"结论：\s*(.+)", response_out)
        additional_info_match = re.search(r"补充信息：\s*(.+)", response_out)

        # 定义结论变量
        conclusion = ""

        # 将找到的内容拼接成一个自然的句子
        if conclusion_match1:
            conclusion += conclusion_match1.group(1)
        
        if additional_info_match:
            conclusion += " " + additional_info_match.group(1)
        
        if conclusion_match2:
            conclusion += " " + conclusion_match2.group(1)

        # 如果结论不为空，返回结论；否则，返回"未查询到"
        if conclusion:
            return jsonify({"output": conclusion}), 200
        else:
            return jsonify({"output": "未查询到"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

