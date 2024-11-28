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
    
    # Ensure input is provided
    if not user_input:
        return jsonify({"error": "No input provided"}), 400
    
    # Invoke agent_executor and get response
    try:
        response = agent_executor.invoke({"input": user_input})
        response_out = response["output"]
        conclusion_match = re.search(r"结论：\s*(.+)", response_out)
        if conclusion_match:
            conclusion = conclusion_match.group(1)
        else:
            conclusion = "未查询到"
        return jsonify({"output": conclusion})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

