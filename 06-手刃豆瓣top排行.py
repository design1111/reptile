import requests
import re

#存如csv格式
import csv

url = "https://movie.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3878.400 QQBrowser/10.8.4518.400"
}
resp = requests.get(url, headers=headers)
page_content = resp.text

#解析数据
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>'  #获取电影名
                 r'.*?<p class="">.*?<br>(?P<year>.*?)&nbsp'                              #获取电影上映年份
                 r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>' #获取电影评分
                 r'.*?<span>(?P<num>.*?)人评价</span>', re.S)
#开始匹配
result = obj.finditer(page_content)
f = open("data.csv", mode="w", encoding="utf-8")
csvwriter = csv.writer(f)

#下面这个循环不注释掉，最后面的循环会出错
# for it in result:
#     print(it.group("name"))
#     print(it.group("year").strip())    #去掉name和year之间的间隔
#     print(it.group("score"))
#     print(it.group("num"))

for i in result:
    dic = i.groupdict()
    dic['year'] = dic['year'].strip()
    csvwriter.writerow(dic.values())
f.close()
resp.close()
print("Over!")
