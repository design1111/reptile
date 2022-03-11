import requests
from lxml import etree
import csv
from concurrent.futures import ThreadPoolExecutor

f = open("线程池_菜价.csv", mode="w", encoding="utf-8")
csvwriter = csv.writer(f)

def download_one_page(url):
    resp = requests.get(url)
    # print(resp.text)
    html = etree.HTML(resp.text)
    #下面要是不加[0]就是一个列表，且只有一个元素，索引为0
    table = html.xpath("/html/body/div[2]/div[4]/div[1]/table")[0]
    # print(table)
    # [1:]每页获取的菜价还有一个 “菜名”  “价格” 之类的东西，[1:]就是用来去除列表第一行元素的
    # trs = table.xpath("./tr")[1:]
    trs = table.xpath("./tr[position()>1]")  #方法二，舍弃第一行的数据
    # print(len(trs))
    #拿到每个tr
    for tr in trs:
        txt = tr.xpath("./td/text()")
        # print(txt)
        #对数据做简单的处理：\\  /去掉
        txt = (item.replace("\\","").replace("/", "") for item in txt)
        # print(list(txt))
        csvwriter.writerow(txt)
    print(url, "提取完毕")

if __name__ == '__main__':
    # download_one_page("https://www.construdip.com/marketanalysis/0/list/1.shtml")

    #单线程的下载方式
    # for i in range(1, 100):
    #     download_one_page(f"https://www.construdip.com/marketanalysis/0/list/{i}.shtml")
    with ThreadPoolExecutor(50) as t:
        for i in range(1, 200):
            #把下载任务提交给线程池
            t.submit(download_one_page, f"https://www.construdip.com/marketanalysis/0/list/{i}.shtml")
