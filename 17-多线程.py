
#多线程
from threading import Thread

def func():
     for i in range(100):
         print("func", i)

if __name__ == '__main__':
    #target=func 不加括号是对函数的调用；target=func()加括号是对结果的调用
    t = Thread(target=func)  # 创建一个多线程对象
    t.start()   #多线程为可以开始工作状态
    for i in range(100):
        print("main", i)



