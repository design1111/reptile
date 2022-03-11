#导入线程池和进程池
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def fn(name):
    for i in range(10):
        print(name, i)
if __name__ == '__main__':
    #创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(10):
            t.submit(fn, name=f"线程{i}")   #调度任务
    #等待线程池中的任务全部执行完毕，才继续执行（守护）
    print("完成")

