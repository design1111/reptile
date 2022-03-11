from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
web = Chrome()
web.get("http://lagou.com")
#关闭弹窗
web.find_element(By.XPATH, '//*[@id="cboxClose"]').click()
time.sleep(1)

#搜索栏搜索python,并进行回车操作
web.find_element(By.XPATH, '//*[@id="search_input"]').send_keys("python", Keys.ENTER)
time.sleep(1)

#点击进入当前岗位，会打开一个新的页面
web.find_element(By.XPATH, '//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').click()

#如何进入到新窗口中进行提取
web.switch_to.window(web.window_handles[-1])

#在新窗口中提取内容
job_detil = web.find_element(By.XPATH, '//*[@id="job_detail"]/dd[2]/div/p').text
print(job_detil)

#关闭子窗口
web.close()
#变更selenium的窗口视角，回到原来的窗口中
web.switch_to.window(web.window_handles[0])
