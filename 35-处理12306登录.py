from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from chaojiying import Chaojiying_Client
import time

#初始化超级鹰
chaojiying = Chaojiying_Client('18392312548', 'leilei123', '929057')

web = Chrome()
web.get("https://kyfw.12306.cn/otn/resources/login.html")
time.sleep(2)
