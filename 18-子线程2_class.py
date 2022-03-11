from threading import Thread

class MyThread(Thread):   #子类继承了Thread
    def run(self):        #这里的方法必须是run()
        for i in range(1000):
            print("子线程", i)

if __name__ == '__main__':
    t = MyThread()  #定义一个对象
    t.start()       #开启线程
    for i in range(1000):
        print("主线程", i)
