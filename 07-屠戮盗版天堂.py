import requests
import re
import time

domain = "https://dytt89.com/"
resp = requests.get(domain, verify=False)  #verify=False：不做访问页面时的校验
resp.encoding = 'gb2312'  #指定字符集
# print(resp.text)

#拿到ul里面的li
obj1 = re.compile(r'2022必看热片.*?<ul>(?P<ul>.*?)</ul>', re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(r'◎片　　名(?P<movie>.*?)<br />'
                  r'.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">', re.S)

result1 = obj1.finditer(resp.text)
child_href_list = []   #创建一个列表
for it in result1:
    ul = it.group('ul')
    # print(ul)
    # 提取子页面链接
    result2 = obj2.finditer(ul)
    for itt in result2:
        # print(itt.group('href'))
        #本句是将https://dytt89.com/ + /i/104951.html 将这个链接拼接起来
        child_href = domain + itt.group('href').strip("/")   #.strip("/")是将链接中多余的一个/去掉
        child_href_list.append(child_href)   #把子页面保存起来

#提取子页面内容
for href in child_href_list:
    child_resp = requests.get(href, verify=False)
    child_resp.encoding = 'gbk'
    result3 = obj3.search(child_resp.text)
    print(result3.group("movie"))
    print(result3.group("download"))
    time.sleep(1)
    # break

