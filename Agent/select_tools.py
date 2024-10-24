from langchain.tools import Tool
from Tools import *

tools = [
    Tool.from_function(
        func=weathercheck,
        name="weather_check",
        description="查询各地天气信息，输入格式：城市名称或坐标（格式为'纬度:经度'）",
        # args_schema=WeatherInput,
    ),
    Tool.from_function(
        func=track,
        name="track_fish",
        description="获得鱼类位移、速度、摆尾次数、加速度，并且你要自己根据这四个指标去判断活跃度，其中都是cm量级的单位，输入格式：鱼类视频（格式为'MP4'）",
        # args_schema=mp4_input,
    )
]

tool_names = [tool.name for tool in tools]
