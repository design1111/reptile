
import requests
import asyncio
import aiohttp
import json
import aiofiles

#1、同步操作：访问getCatalog ，拿到所有章节的cid和名称
#2、异步操作：访问 getChapterContent，下载所有的文章内容
#
# "http://dushu.baidu.com/pc/detail?gid=4306063500"
#
# 'http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}'
async def aiodownload(cid, b_id, title):
    data = {
        "book_id": f"{b_id}",
        "cid": f"{b_id}|{cid}",
        "need_bookinfo": 1
    }
    data = json.dumps(data)   #将data转换为字符串
    url = f"http://dushu.baidu.com/api/pc/getChapterContent?data={data}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()

            async with aiofiles.open("西游记小说/"+title, mode="w", encoding="utf-8") as f:
                await f.write(dic['data']['novel']['content'])


async def getCatalog(url):
    resp = requests.get(url)
    # print(resp.text)
    # print(resp.json())
    dic = resp.json()
    tasks = []
    # 在data里面找到novel，再在novel中找到items；
    for item in dic['data']['novel']['items']:
        title = item['title']  #在items中找到title
        cid = item['cid']
        #准备异步任务
        tasks.append(asyncio.create_task(aiodownload(cid, b_id, title)))
        # print(title, cid)
    await asyncio.wait(tasks)

if __name__ == '__main__':
    b_id = "4306063500"
    # url = 'http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":f"{b_id}"}'  这样写就会报错，只能用下面的
    url = 'http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"' + b_id + '"}'
    asyncio.run(getCatalog(url))

