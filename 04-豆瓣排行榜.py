import requests

# 爬取网站 https://movie.douban.com/typerank?type_name=%E5%96%9C%E5%89%A7&type=24&interval_id=100:90&action=
# 需要加载的js地址：https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20
# #这个连接中？后的为数据
url = "https://movie.douban.com/j/chart/top_list"



# 重新封装参数
param = {
    "type": 24,
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20
}

# resp = requests.get(url=url, params=param)
#
# # 输出地址
# print(resp.request.url)
#
# print(resp.request.headers)

# #重新定义User-Agent
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3878.400 QQBrowser/10.8.4518.400"
}
resp = requests.get(url=url, params=param, headers=header)
print(resp.text)
print(resp.json())
resp.close()   # 关掉resp
