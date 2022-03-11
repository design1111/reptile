import requests

url = "https://www.baidu.com"
#代理ip
proxies = {
    "https://": "https://211.136.128.154:53281"
}

resp = requests.get(url, proxies=proxies)
resp.encoding = "utf-8"
print(resp.text)