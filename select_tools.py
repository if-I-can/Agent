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
    ),
    Tool.from_function(
        func=Calculator,
        name="Calculator",
        description="执行算术运算和计算，输入格式：数学表达式。",
        # args_schema=openmmInput,
    ),
    Tool.from_function(
        func=Canny_text_to_image,
        name="CannyTextToImage",
        description="先将Input翻译为英文，在调用该工具，输入格式：文本生成图像。",
        # args_schema=openmmInput,
    ),
    Tool.from_function(
        func=ImageToCanny,
        name="ImageToCanny",
        description="将图像转换为Canny边缘图像，输入格式：图像URL或本地图片地址。",
        # args_schema=openmmInput,
    ),
    Tool.from_function(
        func=ImageToDepth,
        name="ImageToDepth",
        description="将图像转换为深度图，输入格式：图像URL或本地图片地址。",
        # args_schema=openmmInput,
    ),
    Tool.from_function(
        func=ImageExpansion,
        name="ImageExpansion",
        description="扩展图像的背景，输入格式：图像URL或本地图片地址。",
        # args_schema=openmmInput,
    ),
    Tool.from_function(
        func=HumanBodyPose,
        name="HumanBodyPose",
        description="检测图像中的人体姿势，输入格式：图像URL或本地图片地址。",
        # args_schema=openmmInput,
    ),
    Tool.from_function(
        func=HumanFaceLandmark,
        name="HumanFaceLandmark",
        description="识别图像中的人脸特征点，输入格式：图像URL或本地图片地址。",
        # args_schema=openmmInput,
    ),
    Tool.from_function(
        func=ImageToScribble,
        name="ImageToScribble",
        description="将图像转换为涂鸦风格，输入格式：图像URL或本地图片地址。",
        # args_schema=openmmInput,
    ),
    Tool.from_function(
        func=ScribbleTextToImage,
        name="ScribbleTextToImage",
        description="将涂鸦文本转换为图像，输入格式：涂鸦描述文本。",
        # args_schema=openmmInput,
    ),
    Tool.from_function(
        func=ImageDescription,
        name="ImageDescription",
        description="生成图像的描述文本，输入格式：图像URL或本地图片地址。",
        # args_schema=openmmInput,
    ),
    Tool.from_function(
        func=TextToImage,
        name="TextToImage",
        description="根据文本描述生成图像，输入格式：图像描述文本。",
        # args_schema=openmmInput,
    ),
        Tool.from_function(
        func=ThermalToImage,
        name="ThermalToImage",
        description="将热成像数据转换为可视图像，输入格式：热成像数据。",
        # args_schema=openmmInput,
    ),
    Tool.from_function(
        func=Object_detection,
        name="ObjectDetection",
        description="检测并识别图像中的物体，返回其名字，只用调用一次该工具，输入格式：图像URL或本地图片地址。",
        # args_schema=openmmInput,
    ),
    Tool.from_function(
        func=TextToBbox,
        name="TextToBbox",
        description="根据文本生成边界框，输入格式：文本描述。",
        # args_schema=openmmInput,
    ),
    Tool.from_function(
        func=OCR,
        name="OCR",
        description="识别图像中的文本，输入格式：图像URL或本地图片地址。",
        # args_schema=openmmInput,
    ),
    Tool.from_function(
        func=Segment_anything,
        name="SegmentAnything",
        description="seg the object which I want，输入格式：图像URL或本地图片地址。",
        # args_schema=openmmInput,
    ),
    Tool.from_function(
        func=SegmentObject,
        name="SegmentObject",
        description="分割图像中的特定物体，输入格式：图像URL或本地图片地址和物体描述。",
        # args_schema=openmmInput,
    ),
    Tool.from_function(
        func=SemanticSegmentation,
        name="SemanticSegmentation",
        description="对图像进行语义分割，输入格式：图像URL或本地图片地址。",
        # args_schema=openmmInput,
    ),
    Tool.from_function(
        func=Translation,
        name="Translation",
        description="将输入文本需要翻译的部分翻译。",
        # args_schema=openmmInput,
    ),
    Tool.from_function(
        func=VQA,
        name="VQA",
        description="基于视觉内容回答问题，输入格式：图像URL和问题文本。",
        # args_schema=openmmInput,
    ),
]

tool_names = [tool.name for tool in tools]
