from agentlego import list_tools, load_tool
import argparse

def Calculator(calculation,type=str):
    calculation_tool = load_tool("Calculator",device="cpu")
    result = calculation_tool(calculation)
    return result

def Canny_text_to_image(text,type=str):
    canny_text_to_image = load_tool("Canny_text_to_image",device="cpu")
    result = canny_text_to_image(text)
    return result

def HumanBodyPose(img,type=str):
    canny_text_to_image = load_tool("HumanBodyPose",device="cpu")
    result = canny_text_to_image(img)
    return result

def HumanFaceLandmark(img,type=str):
    canny_text_to_image = load_tool("HumanFaceLandmark",device="cpu")
    result = canny_text_to_image(img)
    return result

def ImageDescription(img,type=str):
    canny_text_to_image = load_tool("ImageDescription",device="cpu")
    result = canny_text_to_image(img)
    return result

def ImageExpansion(img,type=str):
    canny_text_to_image = load_tool("ImageExpansion",device="cpu")
    result = canny_text_to_image(img)
    return result

def ImageToCanny(text,type=str):
    canny_text_to_image = load_tool("ImageToCanny",device="cpu")
    result = canny_text_to_image(text)
    return result

def ImageToDepth(img,type=str):
    canny_text_to_image = load_tool("ImageToDepth",device="cpu")
    result = canny_text_to_image(img)
    return result

def ImageToScribble(img,type=str):
    canny_text_to_image = load_tool("ImageToScribble",device="cpu")
    result = canny_text_to_image(img)
    return result

def Object_detection(img,type=str):
    calculation_tool = load_tool("ObjectDetection",device="cpu")
    result = calculation_tool(img)
    return result

def OCR(img,type=str):
    calculation_tool = load_tool("OCR",device="cpu")
    result = calculation_tool(img)
    return result

def ScribbleTextToImage(text,type=str):
    canny_text_to_image = load_tool("ScribbleTextToImage",device="cpu")
    result = canny_text_to_image(text)
    return result

def Segment_anything(img,type=str):
    calculation_tool = load_tool("SegmentAnything",device="cpu")
    result = calculation_tool(img)
    return result

def SegmentObject(img,type=str):
    calculation_tool = load_tool("SegmentObject",device="cpu")
    result = calculation_tool(img)
    return result

def SemanticSegmentation(img,type=str):
    calculation_tool = load_tool("SemanticSegmentation",device="cpu")
    result = calculation_tool(img)
    return result

def TextToBbox(img,type=str):
    calculation_tool = load_tool("TextToBbox",device="cpu")
    result = calculation_tool(img)
    return result

def TextToImage(text,type=str):
    canny_text_to_image = load_tool("TextToImage",device="cpu")
    result = canny_text_to_image(text)
    return result

def ThermalToImage(txt,type=str):
    calculation_tool = load_tool("ThermalToImage",device="cpu")
    result = calculation_tool.apply(txt,target='en')
    return result

def Translation(txt,type=str):
    calculation_tool = load_tool("Translation",device="cpu")
    result = calculation_tool.apply(txt,target='en')
    return result

def VQA(img,type=str):
    calculation_tool = load_tool("VQA",device="cpu")
    result = calculation_tool(img)
    return result