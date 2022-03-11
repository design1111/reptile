from multiprocessing import Process

def func(name):
    for i in range(10000):
        print(name, i)

if __name__ == '__main__':
    #target=func 表示是对函数的调用；target=func()表示是对结果的调用
    p1 = Process(target=func, args=("周杰伦",))  #传递参数必须是元组
    p1.start()  # 开启多进程
    p2 = Process(target=func, args=("王力宏",))  # 传递参数必须是元组
    p2.start()  # 开启多进程
