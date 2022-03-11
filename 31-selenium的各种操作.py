from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
web = Chrome()
web.get("http://lagou.com")

#找到某个元素，点击它
# el = web.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a')  #旧版本的，新版本如下
el = web.find_element(By.XPATH, '//*[@id="changeCityBox"]/p[1]/a')
el.click()

time.sleep(2)
# 找到输入框，输入python ==> 输入回车/点击搜索按钮
web.find_element(By.XPATH, '//*[@id="search_input"]').send_keys("python", Keys.ENTER)

# 查找存放数据的位置，进行数据提取
# 找到页面中存放数据的所有li
li_list = web.find_elements(By.XPATH, '//*[@id="jobList"]/div[1]/div')
for li in li_list:
    job_name = li.find_element(By.TAG_NAME, "a").text
    job_price = li.find_element(By.XPATH, './div/div/div[2]/span').text
    print(job_price, job_name)
    time.sleep(1)