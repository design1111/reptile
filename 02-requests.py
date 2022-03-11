import requests

# url = 'https://www.baidu.com/s?wd=周杰伦'
url = 'https://www.sogou.com/web?quary=周杰伦'

# headers是一个字典
headers = {
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}
resp = requests.get(url, headers= headers)  #处理一个反爬问题

print(resp)
print(resp.text)   # resp.text 获得网页代码

# =============================================第二种输入方式的==============================================
query = input("请输入一个要搜索的明星姓名")

url = f'https://www.sogou.com/web?quary={query}'

# headers是一个字典
headers = {
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}
resp = requests.get(url, headers= headers)  #处理一个反爬问题

print(resp)
print(resp.text)