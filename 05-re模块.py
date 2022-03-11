import re

#findall:匹配字符串中所有的符合正则的内容
lst = re.findall("\d+", "我的电话号是：10086, 我女朋友的是: 10010")
print(lst)

#这里加了一个r
lst1 = re.findall(r"\d+", "我的电话号是：10086, 我女朋友的是: 10010")
print(lst1)

#finditer: 匹配字符串中s所有的内容[返回的是迭代器],从迭代器中拿到的内容需要.group()
it = re.finditer(r"\d+", "我的电话号是：10086, 我女朋友的是: 10010")
print(it)
for i in it:
    print(i)
    print(i.group())

# search,找到一个结果就返回，返回的结果是match对象，拿数据需要.group()
s = re.search(r"\d+", "我的电话号是：10086, 我女朋友的是: 10010")
print(s.group())

#match是从头开始匹配
s = re.match(r"\d+", "10086, 我女朋友的是: 10010")
print(s.group())

# 预加载z正则表达式
obj = re.compile(r"\d+")
ret = obj.finditer("我的电话号是：10086, 我女朋友的是: 10010")
for j in ret:
    print(j.group())

S = """
<div class='jar'><span id='1'>郭麒麟</span></div>
<div class='re'><span id='1'>sfds</span></div>
<div class='ff'><span id='1'>grd</span></div>
<div class='jar'><span id='1'>郭麒麟</span></div>
"""

#  (?P<分组名字>正则)   可以单独从z正则匹配d的内容中提取到xxx名字的内容
obj1 = re.compile(r"<div class=‘.*?'><span id='\d+'>.*?</span></div>", re.S)   # re.S:  让.能匹配换行符

result = obj1.finditer(S)
for j1 in result:
    print(j1.group())

