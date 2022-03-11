import asyncio
import time

async def func1():
    print("程序1")
    # time.sleep(3) #当程序出现了同步操作的时候，异步就中断了
    await asyncio.sleep(3)  #异步操作的代码;await表示挂起，cpu执行下一个程序
    print("程序1")
async def func2():
    print("程序2")
    # time.sleep(2)
    await asyncio.sleep(2)
    print("程序2")
async def func3():
    print("程序3")
    # time.sleep(4)
    await asyncio.sleep(4)
    print("程序3")

async def main():
    #第一种写法
    # f1 = func1()
    # await f1   #一般await挂起操作放在协程对象前面
    #第二种写法
    tasks = [asyncio.create_task(func1()), asyncio.create_task(func2()), asyncio.create_task(func3())]
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())