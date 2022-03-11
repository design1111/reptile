import requests
# session可以认为是一连串的请求，在这个过程中cookie不会丢
# 会话
session = requests.session()
data = {
    "loginName": "18614075987",
    "password": "q6035945"
}

#1、登录
url = "https://passport.17k.com/ck/user/login"
# resp = session.post(url, data=data)
session.post(url, data=data)
# print(resp.text)
# print(resp.cookies)

#2、拿书架上的数据
resp = session.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919')
# print(resp.text)
print(resp.json())
