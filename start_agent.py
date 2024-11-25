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


class react_agent:
    def __init__(self, system_prompt_path="/home/zsl/Agent/Data/prompt.txt",api_key="sk-027ac6afb5bc4cfb8ccb0b51fc3c5b26", model_name="deepseek-chat", api_base="https://api.deepseek.com"):
        # 读取 system_prompt 文档
        self.system_prompt = self.load_system_prompt(system_prompt_path)
        
        # 设置回调处理器
        self.callback = CustomAsyncIteratorCallbackHandler()

        # 初始化DeepSeek模型
        self.model = ChatOpenAI(
            model_name=model_name,
            verbose=True,
            callbacks=[self.callback],
            temperature=0.0,
            openai_api_base=api_base,
            openai_api_key=api_key,
        )

        # 配置Prompt模板和链
        self.prompt_template_agent = CustomPromptTemplate(
            template=self.system_prompt, tools=tools, input_variables=["input", "intermediate_steps", "history"]
        )
        self.llm_chain = LLMChain(llm=self.model, prompt=self.prompt_template_agent)

        # 输出解析器
        self.output_parser = CustomOutputParser()

        # 创建Agent
        self.react_agent = LLMSingleActionAgent(
            llm_chain=self.llm_chain,
            output_parser=self.output_parser,
            stop=["\nObservation:", "Observation"],
            allowed_tools=tool_names,
        )

        # 设置内存
        self.memory = ConversationBufferWindowMemory(k=0)

        # 创建AgentExecutor
        self.agent_executor = AgentExecutor.from_agent_and_tools(
            agent=self.react_agent,
            tools=tools,
            verbose=True,
            memory=self.memory,
        )

    def load_system_prompt(self, path):
        """从文件中加载 system_prompt"""
        with open(path, "r") as f:
            return f.read()

    def invoke(self, input_text):
        """通过代理执行输入任务并返回结果"""
        return self.agent_executor.invoke(input_text)

    def add_tools(self, new_tools):
        """向现有代理添加工具"""
        self.react_agent.allowed_tools.extend(new_tools)

    def set_memory_window(self, k):
        """设置内存窗口的大小"""
        self.memory.k = k

    def get_agent_info(self):
        """获取当前代理的基本信息"""
        return {
            "model_name": self.model.model_name,
            "api_base": self.model.openai_api_base,
            "allowed_tools": self.react_agent.allowed_tools,
            "memory_window": self.memory.k,
        }


# 示例用法
if __name__ == "__main__":
    # 初始化代理管理器
    agent_manager = react_agent()

    # 执行任务
    result = agent_manager.invoke("检测图像/home/zsl/Agent/generated/image/20241119_d6ed.png")
    print("Result:", result)


