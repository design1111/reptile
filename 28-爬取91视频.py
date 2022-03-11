import requests
import re
import csv
#因为这里的url是在javascript中，就不能使用xpath，只能使用re来提取
obj = re.compile(r"url: '(?P<url>.*?)',", re.S)  #用来提取m3u8的地址


url = "http://91kanju2.com/vod-play/54812-2-1.html"
resp = requests.get(url)
# print(resp.text)
m3u8_url = obj.search(resp.text).group("url")
# print(m3u8_url)  #输出为：https://mv.cbi88.com/20201213/8poeNTvr/index.m3u8
resp.close()

# #下载m3u8文件
# try:
#     resp2 = requests.get(m3u8_url)
# except requests.exceptions.ConnectionError:
#     requests.status_code = "Connection refused"

proxies = {
    "https://": "https://101.34.214.152:8001"
}
# 很有可能是网络不好造成的下面不能够访问到
resp2 = requests.get(m3u8_url, proxies=proxies, timeout=30, verify=False)

with open("哲仁王后.m3u8", mode="wb") as f:
    f.write(resp2.content)

resp2.close()
print("下载完毕")

