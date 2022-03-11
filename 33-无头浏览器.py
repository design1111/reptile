from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
#引入下拉选择的包
from selenium.webdriver.support.select import Select
import time
#浏览器在后台操作
from selenium.webdriver.chrome.options import Options

#准备好参数配置
opt = Options()
opt.add_argument("--headless")  #无头操作
opt.add_argument("--disable-gpu")  #不让gpu渲染


web = Chrome(options=opt)
web.get("https://www.endata.com.cn/BoxOffice/BO/Year/index.html")

#定位到下拉页表
sel_el = web.find_element(By.XPATH, '//*[@id="OptionDate"]')
#对元素进行包装，包装成下拉菜单
sel = Select(sel_el)

#让浏览器进行调整选项
for i in range(len(sel.options)):
    sel.select_by_index(i)   #按照索引进行切换
    time.sleep(2)
    table = web.find_element(By.XPATH, '//*[@id="TableList"]/table')
    print(table.text)
    print("===================================================")
print("运行完毕")
web.close()

# 如何拿到页面代码Elements(经过数据加载以及js执行之后的结果的html内容)
print(web.page_source)