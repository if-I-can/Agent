from collections import deque

from colorama import Fore
from graphviz import Digraph  # type: ignore

from mul_agent_depend.logging import fancy_print


class Crew:
    """
    表示一起工作的代理人员的类。

    此类管理一组代理、它们的依赖关系，并提供以拓扑排序顺序运行代理的方法。

    属性:
        current_crew (Crew): 类级变量，用于跟踪活动的 Crew 上下文。
        agents (list): Crew 中的代理列表。
    """

    current_crew = None

    def __init__(self):
        self.agents = []

    def __enter__(self):
        """
        进入上下文管理器，将此 Crew 设置为当前活动上下文。

        返回:
            Crew: 当前的 Crew 实例。
        """
        Crew.current_crew = self
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        退出上下文管理器，清除活动上下文。

        参数:
            exc_type: 异常类型（如果引发了异常）。
            exc_val: 异常值（如果引发了异常）。
            exc_tb: 回溯（如果引发了异常）。
        """
        Crew.current_crew = None

    def add_agent(self, agent):
        """
        将代理添加到 Crew。

        参数:
            agent: 要添加到 Crew 的代理。
        """
        self.agents.append(agent)

    @staticmethod
    def register_agent(agent):
        """
        向当前活动的 Crew 上下文注册代理。

        参数:
            agent: 要注册的代理。
        """
        if Crew.current_crew is not None:
            Crew.current_crew.add_agent(agent)

    def topological_sort(self):
        """
        根据代理的依赖关系对代理执行拓扑排序。

        返回:
            list: 以拓扑顺序排序的代理列表。

        引发:
            ValueError: 如果代理之间存在循环依赖关系。
        """
        in_degree = {agent: len(agent.dependencies) for agent in self.agents}
        queue = deque([agent for agent in self.agents if in_degree[agent] == 0])

        sorted_agents = []

        while queue:
            current_agent = queue.popleft()
            sorted_agents.append(current_agent)

            for dependent in current_agent.dependents:
                in_degree[dependent] -= 1
                if in_degree[dependent] == 0:
                    queue.append(dependent)

        if len(sorted_agents) != len(self.agents):
            raise ValueError("检测到代理之间存在循环依赖关系，阻止了有效的拓扑排序")

        return sorted_agents

    def plot(self):
        """
        使用 Graphviz 绘制 Crew 中代理的有向无环图 (DAG)。

        返回:
            Digraph: 表示代理依赖关系的 Graphviz Digraph 对象。
        """
        dot = Digraph(format="png")  # 将格式设置为 PNG 以进行内联显示

        # 为 Crew 中的每个代理添加节点和边
        for agent in self.agents:
            dot.node(agent.name)
            for dependency in agent.dependencies:
                dot.edge(dependency.name, agent.name)
        return dot

    def run(self):
        """
        以拓扑排序顺序运行 Crew 中的所有代理。

        此方法执行每个代理的 run 方法并打印结果。
        """
        sorted_agents = self.topological_sort()
        for agent in sorted_agents:
            fancy_print(f"正在运行代理: {agent}")
            print(Fore.RED + f"{agent.run()}")
