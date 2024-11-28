from typing import List, Union
from textwrap import dedent

from mul_agent_depend import Crew
from start_agent import react_agent
from mul_agent_depend.tool import Tool
from reflect_agent import reflect_agent


class Agent:
    """
    Represents an AI agent that can work as part of a team to accomplish a task.

    This class implements an agent with dependencies, context handling, and task execution capabilities.
    It can be used in a multi-agent system, where agents collaborate to solve complex problems.
    Currently supports two agent types: ReactAgent and ReflectionAgent.

    Attributes:
        name (str): The name of the agent.
        backstory (str): The backstory or background of the agent.
        task_description (str): The description of the task assigned to the agent.
        task_expected_output (str): The expected format or content of the task output.
        agent: An instance of either ReactAgent or ReflectionAgent.
        dependencies (list[Agent]): A list of Agent instances that this agent depends on.
        dependents (list[Agent]): A list of Agent instances that depend on this agent.
        context (str): The accumulated context information from other agents.

    Args:
        name (str): The name of the agent.
        backstory (str): The backstory or background of the agent.
        task_description (str): The description of the task assigned to the agent.
        task_expected_output (str, optional): The expected format or content of the task output. Defaults to "".
        tools (Union[Tool, List[Tool]]): A list of Tool instances or a single Tool instance available to the agent. Defaults to None.
        llm (str, optional): The name of the language model to use. Defaults to "Qwen/Qwen2.5-72B-Instruct".
        use_reflection (bool, optional): Whether to use a ReflectionAgent instead of a ReactAgent. Defaults to False.
        zhipuai (bool, optional): Whether to use the ZhipuAI API when using a ReflectionAgent. Defaults to False.
        reflection_steps (int, optional): The number of reflection steps when using a ReflectionAgent. Defaults to 3.
    """

    def __init__(
        self,
        name: str,
        backstory: str,
        task_description: str,
        task_expected_output: str = "",
        tools: Union[Tool, List[Tool]] = None,
        use_reflection: bool = False,
        reflection_steps: int = 3,
    ):
        self.name = name
        self.backstory = backstory
        self.task_description = task_description
        self.task_expected_output = task_expected_output
        self.reflection_steps = reflection_steps

        # Ensure tools is a list
        if isinstance(tools, Tool):
            tools = [tools]

        # Choose which agent to use based on use_reflection
        if use_reflection:
            self.agent = reflect_agent()
        else:
            self.agent = react_agent
        print("=====", tools) 
        self.dependencies: list[Agent] = []  # Agents this agent depends on
        self.dependents: list[Agent] = []  # Agents that depend on this agent
        self.context = ""

        # Automatically register this agent to the active Crew context if one exists
        Crew.register_agent(self)

    def __repr__(self):
        return f"{self.name}"

    def __rshift__(self, other):
        """
        Defines the '>>' operator. This operator is used to indicate agent dependency.

        Args:
            other (Agent): The agent that depends on this agent.
        """
        self.add_dependent(other)
        return other  # Allows chaining

    def __lshift__(self, other):
        """
        Defines the '<<' operator to indicate agent dependency in reverse.

        Args:
            other (Agent): The agent that this agent depends on.

        Returns:
            Agent: The `other` agent, allowing chaining.
        """
        self.add_dependency(other)
        return other  # Allows chaining

    def __rrshift__(self, other):
        """
        Defines the '<<' operator. This operator is used to indicate agent dependency.

        Args:
            other (Agent): The agent that this agent depends on.
        """
        self.add_dependency(other)
        return self  # Allows chaining

    def __rlshift__(self, other):
        """
        Defines the '<<' operator when evaluated from right to left.
        This operator is used to indicate agent dependency in normal order.

        Args:
            other (Agent): The agent that depends on this agent.

        Returns:
            Agent: The current agent (self), allowing chaining.
        """
        self.add_dependent(other)
        return self  # Allows chaining

    def add_dependency(self, other):
        """
        Adds a dependency to this agent.

        Args:
            other (Agent | list[Agent]): The agent or list of agents this agent depends on.

        Raises:
            TypeError: If the dependency is not an Agent or list of Agents.
        """
        if isinstance(other, Agent):
            self.dependencies.append(other)
            other.dependents.append(self)
        elif isinstance(other, list) and all(isinstance(item, Agent) for item in other):
            for item in other:
                self.dependencies.append(item)
                item.dependents.append(self)
        else:
            raise TypeError("Dependencies must be an instance or list of Agent.")

    def add_dependent(self, other):
        """
        Adds a dependent to this agent.

        Args:
            other (Agent | list[Agent]): The agent or list of agents that depend on this agent.

        Raises:
            TypeError: If the dependency is not an Agent or list of Agents.
        """
        if isinstance(other, Agent):
            other.dependencies.append(self)
            self.dependents.append(other)
        elif isinstance(other, list) and all(isinstance(item, Agent) for item in other):
            for item in other:
                item.dependencies.append(self)
                self.dependents.append(item)
        else:
            raise TypeError("Dependencies must be an instance or list of Agent.")

    def receive_context(self, input_data):
        """
        Receives and stores context information from other agents.

        Args:
            input_data (str): The context information to add.
        """
        self.context += f"{self.name} received context: \n{input_data}"

    def create_prompt(self):
        """
        Creates a prompt for the agent based on its task description, expected output, and context.

        Returns:
            str: The formatted prompt string.
        """
        prompt = dedent(
            f"""
            You are an AI agent. You are part of a team working with other agents to accomplish a task.
            I will provide you with the description of your task enclosed in <task_description></task_description> tags. I will also provide you with
            the available context from other agents in the <context></context> tags. If no context is available,
            the <context></context> tags will be empty. You will also receive the expected output of your task enclosed in 
            <task_expected_output></task_expected_output> tags.
            With all this information, you need to create the best possible response, always following the format described in the <task_expected_output></task_expected_output> tags. 
            If no expected output is available, just create a sensible response to complete the task.

            <task_description>
            {self.task_description}
            </task_description>

            <task_expected_output>
            {self.task_expected_output}
            </task_expected_output>

            <context>
            {self.context}
            </context>

            Your response:
            """
        ).strip()

        return prompt


    def run(self):
        """
        Runs the agent's task and generates output.

        This method creates a prompt, runs it through the chosen agent (ReactAgent or ReflectionAgent),
        and passes the output to any dependent agents.

        Returns:
            str: The output generated by the agent.
        """
        msg = self.create_prompt()

        # 根据agent类型选择不同的运行方式
        if isinstance(self.agent, reflect_agent):
            output = self.agent.run(
                user_msg=msg,
                generation_system_prompt=self.backstory,
                n_steps=self.reflection_steps,
            )
        else:
            print("msg:", msg)
            self.agent = react_agent()
            output = self.agent.invoke(input_text=msg)

        # 将输出传递给所有依赖项
        for dependent in self.dependents:
            dependent.receive_context(output)
        return output
