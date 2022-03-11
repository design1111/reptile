import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.construdip.com/marketanalysis/0/list/1.shtml"
resp = requests.get(url)
# print(resp.text)

#解析数据
#1、把页面源代码交给BeautifulSoup进行处理，生成bs对象
page = BeautifulSoup(resp.text, "html.parser")   #指定html解析器
#2、从bs对象中查找数据
# find(标签，属性=值)
# find_all(标签，属性=值)
# table = page.find("table", class_="hq_table")  #class是python中的关键字
table = page.find("table", attrs={"class": "hq_table"})  #和上面的语句相同，使用字典的形式
# print(table)

#建立一个文件
f = open("菜价.csv", mode="w", encoding="utf-8")
csvwriter = csv.writer(f)

#拿到所有数据行
trs = table.find_all("tr")[1:]
for tr in trs:   #每一行
    tds = tr.find_all("td")   #拿到每一行中的所有td
    name = tds[0].text       #.text 表示拿到被标签标记的内容
    low = tds[1].text
    avg = tds[2].text
    high = tds[3].text
    gui = tds[4].text
    kind = tds[5].text
    date = tds[6].text
    csvwriter.writerow([name, low, avg, high, gui, kind, date])
f.close()
print("Over")
