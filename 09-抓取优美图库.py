# 1、拿到主页面的源代码，然后提取到子页面的链接地址，href
# 2、通过href拿到子页面的内容，从子页面中找到图片的下载地址  img->src
# 3、下载图片
import requests
from bs4 import BeautifulSoup
import time  #防止频繁访问服务器被封号

url = "https://umei.net/bizhitupian/weimeibizhi/"
resp = requests.get(url)
resp.encoding = 'utf-8'
# print(resp.text)

#把源代码交给bs
main_page = BeautifulSoup(resp.text, "html.parser")
alist = main_page.find("div", class_="TypeList").find_all("a")   #把范围第一次缩小
# print(alist)
for a in alist:
    # print(url + a.get('href').strip("bizhitupian/weimeibizhi/")+"htm")  #直接通过get就可以拿到属性的值
    href = url + a.get('href').strip("bizhitupian/weimeibizhi/")+"htm"
    # print(href)
    # 拿到子页面的源代码
    child_page_resp = requests.get(href)
    child_page_resp.encoding = "utf-8"
    child_page_text = child_page_resp.text
    # 从子页面中拿到图片的x下载路径
    child_page = BeautifulSoup(child_page_text, "html.parser")
    div = child_page.find("div", class_="ImageBody")
    img = div.find("img")  #把范围缩小到img的属性中
    # print(img.get("src"))
    src = img.get("src")  #拿到网页中src中的属性
    #下载图片
    img_resp =requests.get(src)
    img_name = src.split("/")[-1]   #拿到url中的最后一个/之后的内容
    with open("img/"+ img_name, mode="wb") as f:    #加上这个"img/"+ 就开始报错了；必须手动建立一个img文件夹
    # with open("img/" + img_name, mode="wb") as f:
        f.write(img_resp.content)  #图片内容写入文件；img_resp.content 拿到的是图片的字节

    print("Over!", img_name)
    time.sleep(1)
f.close()
child_page_resp.close()
print("All Over!!")



