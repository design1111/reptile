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

if __name__ == '__main__':
    f1 = func1()
    f2 = func2()
    f3 = func3()
    #把任务放到列表里面去
    tasks = [f1, f2, f3]
    t1 = time.time()
    #一次性启动多个任务(协程)
    asyncio.run(asyncio.wait(tasks))
    t2 = time.time()
    print(t2-t1)