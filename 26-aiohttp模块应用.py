import asyncio
import aiohttp

urls = [
    "http://kr.shanghai-jiuxin.com/file/2020/1031/small774218be86d832f359637ab120eba52d.jpg",
    "http://kr.shanghai-jiuxin.com/file/2020/1031/small563337d07af599a9ea64e620729f367e.jpg",
    "http://kr.shanghai-jiuxin.com/file/2020/1031/small26b7e178e987be6d914bf8d1af120890.jpg"
]
async def aiodownload(url):
    name = url.rsplit("/", 1)[1]   #创建文件名为最后一个
    #这里加了with就相当于开文件时的一样，执行完这里之后就不用手动进行释放了
    #aiohttp.ClientSession() <==> 相当于 requests模块
    async with aiohttp.ClientSession() as session:  #async表示异步
        async with session.get(url) as resp:
            # resp.content.read()    #<==>等价于requests模块中的 resp.content
            #请求回来了，写入文件
            with open(name, mode="wb") as f:
                f.write(await resp.content.read())  #读取内容是异步的，需要await挂起
    print(name, "搞定")

async def main():
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(aiodownload(url)))
        # tasks.append(aiodownload(url))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    # asyncio.run(main())  #这里的会报错
    asyncio.get_event_loop().run_until_complete(main())