from langchain.tools import Tool
from Tools import *

tools = [
    Tool.from_function(
        func=weathercheck,
        name="weather_check",
        description="查询各地天气信息，输入格式：城市名称或坐标（格式为'纬度:经度'）",
        args_schema=WeatherInput,
    ),
    Tool.from_function(
        func=mumudet,
        name="mumudet",
        description="精确识别并计数图像中的物体，如羊、鱼、种子等，输入格式：图片URL或本地图片地址,动物类型(英文) ",
        args_schema=MumuDetInput,
    ),
    Tool.from_function(
        func=mumutrack,
        name="fish_tracking",
        description="通过跟踪鱼类进行视频分析，输入格式：视频URL或本地视频地址",
        args_schema=MumuTrackInput,
    ),
    Tool.from_function(
        func=fish_decise,
        name="Fish Feeding Decision",
        description="为鱼类投喂决策提供建议，输入格式：查询内容（请确保查询包含所有必要信息,包括各个有效的数据）",
        args_schema=DecisionInput,
    ),
    Tool.from_function(
        func=search_internet,
        name="search_internet",
        description="进行实时网络搜索,获取最新信息、新闻、数据等。适用于查询时事、市场行情、技术动态等实时性强的信息,输入:搜索关键词。",
        args_schema=SearchInternetInput,
    ),
]

tool_names = [tool.name for tool in tools]
