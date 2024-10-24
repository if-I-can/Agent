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

# read from _prompt.txt as system_prompt
with open("/home/zsl/Agent/Agent/Data/prompt.txt", "r") as f:
    system_prompt = f.read()

#解析system_promot文档   其中intermediate_steps是中间步骤
prompt_template_agent = CustomPromptTemplate(template=system_prompt,tools=tools,input_variables=["input", "intermediate_steps", "history"],)

# 根据用户输入得到规划
callback = CustomAsyncIteratorCallbackHandler()

# 生成答案的模型需求
model = ChatOpenAI(
    model_name="deepseek-chat",  # Replace with the correct DeepSeek model name
    verbose=True,
    callbacks=[callback],
    temperature=0.0,
    openai_api_base="https://api.deepseek.com",  # Directly set the DeepSeek API base URL
    openai_api_key="sk-027ac6afb5bc4cfb8ccb0b51fc3c5b26",  # Directly set the DeepSeek API key
)


llm_chain = LLMChain(llm=model, prompt=prompt_template_agent)
output_parser = CustomOutputParser()
# plant_json = re.sub(r"^```json\s*|\s*```$", "", plan_text, flags=re.MULTILINE)
agent = LLMSingleActionAgent(
    llm_chain=llm_chain,
    output_parser=output_parser,
    stop=["\nObservation:", "Observation"],
    allowed_tools=tool_names,
)

memory = ConversationBufferWindowMemory(k=0)
agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent,
    tools=tools,
    verbose=True,
    memory=memory,
)


# response = agent_executor.invoke({"input": "杭州天气怎么样？"})
# print("输入：",response["input"])
# print("回答：",response["output"])
# print("历史记忆：",response["history"])


response = agent_executor.invoke({"input": "该视频里鱼的四个行为参数/home/zsl/Agent/Agent/fish.mp4"})
print("输入：",response["input"])
print("回答：",response["output"])
print("历史记忆：",response["history"])

