from multiprocessing import Process

def func():
    for i in range(10000):
        print("子进程", i)

if __name__ == '__main__':
    #target=func 表示是对函数的调用；target=func()表示是对结果的调用
    p = Process(target=func)
    p.start()  # 开启多进程
    for i in range(10000):
        print("主进程", i)