#1、拿到contID
#2、拿到videoStatus返回的json. -> srcURL
#3、srcURL 里面的内容进行修整
#4、下载视频

import requests
url = "https://www.pearvideo.com/video_1681528"
contID = url.split("_")[1]  #拿取到_之后的内容1681528
# print(contID)

#要把这个地址里面的内容进行修改
videoStatusURL = f"https://www.pearvideo.com/videoStatus.jsp?contId={contID}&mrd=0.29587422804361174"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3878.400 QQBrowser/10.8.4518.400",
    # 防盗链
    "Referer": "https://www.pearvideo.com/video_1681528"
}
resp = requests.get(videoStatusURL, headers=headers)
# print(resp.json())
# resp.json()['videoInfo']['videos']['srcUrl']
dic = resp.json()
# print(dic)
srcUrl = dic['videoInfo']['videos']['srcUrl']  #拿取到videoInfo中的videos里面的地址srcUrl
# print(srcUrl)
systemTime = dic['systemTime']  #拿取到systemTime的值，值是1645192834127，要把这个值是1645192834127替换为cont-1681528
srcUrl = srcUrl.replace(systemTime, f"cont-{contID}")
# print(srcUrl)

#下载视频
with open("a.mp4", mode="wb") as f:
    f.write(requests.get(srcUrl).content)