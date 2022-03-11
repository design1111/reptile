

from selenium.webdriver import Chrome

web = Chrome()

web.get("http://www.baidu.com")
print(web.title)