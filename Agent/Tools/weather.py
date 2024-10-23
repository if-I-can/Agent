import sys
sys.path.insert(0, "/home/wch/3.8t_1/Workspace/wch/PROJECT/langchainchat")
from pydantic import BaseModel, Field
import requests

GET_CITY_API_KEY = "ZKCsMCKEAWOODltWCf7UqXwkBjYxUoqF"   #这个是百度的根据经纬度差查询城市的api
SENIVERSE_API_KEY = "SFsNGm2ont1sa0yTv"   #这个是心知的根据城市查询天气的api  

#函数2  根据经纬度/城市去查询天气
def weather(location: str, api_key: str):
    if ":" in location:  # 检查输入是否为经纬度格式
        lng = location.split(":")[0]
        lat = location.split(":")[-1]
        print("====",lng,lat)
        url = f"https://api.map.baidu.com/reverse_geocoding/v3/?ak={GET_CITY_API_KEY}&output=json&coordtype=wgs84ll&location={lat},{lng}"
        response = requests.get(url)
        result = response.json()
        location = result['result']['addressComponent']['city']
    url = f"https://api.seniverse.com/v3/weather/daily.json?key={api_key}&location={location}&language=zh-Hans&unit=c&start=0&days=5"
    
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to retrieve weather: {response.status_code}")

# 函数1 调用weather
def weathercheck(location: str):
    return weather(location, SENIVERSE_API_KEY)


if __name__ == "__main__":
    print(weathercheck("合肥"))
    print(weathercheck("117.283042:31.86119"))    