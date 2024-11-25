import requests
import urllib.parse
import json

def test_headers_only(doi):
    encoded_doi = urllib.parse.quote(doi)
    # api_url = f"https://api.crossref.org/works"   # 官方的api_url
    api_urls = f"https://api.crossref.org/works?filter=has-full-text:true&mailto=1786293993@qq.com"

    try:
        response = requests.head(api_urls)
        if response.status_code == 200:
            print(response.headers)  # 仅返回响应的头部信息
        else:
            print(f"请求失败，状态码: {response.status_code}")
    except Exception as e:
        print(f"发生错误: {e}")


def title_doi_journal(keyword, rows):
    # 构建查询 URL，使用 query 参数根据关键词检索，并限制返回的文献数量
    api_url = f"https://api.crossref.org/works?query={keyword}&filter=has-full-text:true&rows={rows}&mailto=1786293993@qq.com"
    
    try:
        # 发送请求到 Crossref API
        response = requests.get(api_url)
        
        # 检查响应状态
        if response.status_code == 200:
            # 解析 JSON 响应
            data = response.json()
            
            # 提取文献信息
            works = data["message"].get("items", [])
            results = []
            for work in works:
                doi = work.get("DOI", "No DOI")
                results.append(doi)
            print("cressref调用成功")
            print(results)
            return results
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None



# 主函数
if __name__ == "__main__":
    test_headers_only("")  # 测试公开的crossref的api_url是否可用   函数1
    search_results = title_doi_journal("fish feeding behaviour and deep learning",rows=100)     #  函数2 返回title doi jornal score year abstract