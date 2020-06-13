import time
from multiprocessing import Pool

def proc(num):
    print("当前进程编号是：{0} 开始执行".format(num))
    time.sleep(5)
    print("当前进程编号是：{0} 执行完毕".format(num))

if __name__ == "__main__":
    pool = Pool(3)
    print("创建5个进程")
    for i in range(5):
        pool.apply_async(proc, args=(i, ))
    pool.close()
    pool.join()
    print("主进程执行完毕！")
