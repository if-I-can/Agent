from openai import OpenAI
import json
import os 

class ChatHistory(list):
    def __init__(self, messages=None, total_length: int = -1):
        if messages is None:
            messages = []
        super().__init__(messages)
        self.total_length = total_length

    def append(self, msg: str):
        if self.total_length > 0 and len(self) >= self.total_length:
            self.pop(0)
        super().append(msg)


class FixedFirstChatHistory(ChatHistory):
    def append(self, msg: str):
        if self.total_length > 0 and len(self) >= self.total_length:
            self.pop(1)
        super().append(msg)

BASE_GENERATION_SYSTEM_PROMPT = """
你的任务是为用户请求生成最佳内容。
如果用户提供了批评，请修改并输出你之前的尝试。
你必须始终输出修改后的内容。
"""

BASE_REFLECTION_SYSTEM_PROMPT = """
你的任务是生成用户生成内容的批评和建议。
如果用户内容有错误或需要改进的地方，输出建议和批评的列表。
如果用户的内容没有问题且不需要更改，输出：[yes]。
"""

class QAagent():
    def __init__(self,model="deepseek-chat"):
        self.clint = OpenAI(base_url = os.getenv("OPENAI_API_BASE"),api_key = os.getenv("OPENAI_API_KEY"))
        self.model = model
    

    def generate(self, generation_history: list, verbose = 0) -> str:
        response = self.clint.chat.completions.create(messages = generation_history,model = self.model)
        return str(response.choices[0].message.content)


    def reflect(self, reflection_history: list, verbose: int = 0) -> str:
        response = self.clint.chat.completions.create(messages = reflection_history,model = self.model)
        return str(response.choices[0].message.content)
    

    def run(self,user_msg,generation_system_prompt = "",reflection_system_prompt = "",n_steps = 3,verbose = 0):
        final_response = []

        generation_system_prompt += BASE_GENERATION_SYSTEM_PROMPT
        reflection_system_prompt += BASE_REFLECTION_SYSTEM_PROMPT

        dict_gen1 = {"content":generation_system_prompt, "role":"system"}
        dict_gen2 = {"content":user_msg, "role":"user"}
        dict_ref = {"content":reflection_system_prompt,"role":"system"}
        
        generation_history = FixedFirstChatHistory([dict_gen1,dict_gen2],total_length=3,)   # 实例化生成的history类
        reflection_history = FixedFirstChatHistory([dict_ref],total_length=3,)   # 实例化反思的history类

        for i in range(n_steps):
            generation = self.generate(generation_history)
            print(generation)
            final_response.append(generation)
            generation_history.append({"content":generation,"role":"assistant"})
            reflection_history.append({"content":generation,"role":"user"})
            critique = self.reflect(reflection_history)
            print(critique)
            final_response.append(critique)
            if "[yes]" in critique:
                break

            generation_history.append({"content":critique,"role":"assistant"})
            reflection_history.append({"content":critique,"role":"user"})
        
        return generation_history[-1]["role"]

agent = QAagent()
           
user_msg = "大口黑鲈的投喂策略"
generation_system_prompt = ("你是一位水产养殖饲料投喂专员，请帮我给出一些饲料投喂建议,每次回答时前面加上（投喂专员:）")
reflection_system_prompt = "你是专业的水产养殖专家，请对一个普通水产养殖专员提出的投喂建议进行批判,语气可以强烈一点，每次回答时前面加上（专家：）"

final_response = agent.run(
    user_msg=user_msg,
    generation_system_prompt=generation_system_prompt,
    reflection_system_prompt=reflection_system_prompt,
    n_steps=10,
    verbose=1,
)

print(final_response)