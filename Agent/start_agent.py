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
with open("/home/zsl/Agent/Data/prompt.txt", "r") as f:
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
print(
    agent_executor.invoke(
        {"input": "杭州天气怎么样？"
        }
    )
)
# print(
#     agent_executor.invoke(
#         {
#             "input": "/home/wch/3.8t_1/Workspace/wch/data/数据集/med/med1/m1/m1_00000.png 里面有多少条鱼"
#         }
#     )
# )
# print(
#     agent_executor.invoke(
#         {
#             "input": "/home/wch/3.8t_1/Workspace/wch/fish_llm/langchainchat/fish.mp4 分析下视频里鱼的运动状态"
#         }
#     )
# )

# print(
#     agent_executor.invoke(
#         {
#             "input": "位移: 1100.6507699115045 cm, 速度: 25.38264690265487 cm/s, 摆尾速度: 259.6637168141593 Hz, 加速度: 680.922315929204 cm/s²,平均检测到的鱼数量: 23  这是鱼的运动状态给我鱼的投喂策略"
#         }
#     )
# )

# print(agent_executor.invoke({"input": "2024年诺贝奖得主是谁"}))

