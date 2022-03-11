from lxml import etree

tree = etree.parse("a.html", etree.HTMLParser())
result = tree.xpath("/html/body/ul/li[1]/a/text()")   #li标签的第一个,[]表示索引
print(result)
result2 = tree.xpath("/html/body/ol/li/a[@href='dapao']/text()")  #[@xxx=xxx] 属性的筛选
print(result2)
print("下面是循环的操作")
ol_li_list = tree.xpath("/html/body/ol/li")
for li in ol_li_list:
    result = li.xpath("./a/text()") #在li中继续查找，相对查找
    print(result)
    result2 = li.xpath("./a/@href") #拿到属性值，通过@
    print(result2)