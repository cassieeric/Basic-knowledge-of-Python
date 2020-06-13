import time
import os
import multiprocessing

def new_process(para):
    time.sleep(1)
    print("子进程ID：{0}".format(os.getpid()))
    print("子进程传进来的参数：{0}".format(para))

if __name__ == "__main__":
    print("父进程的ID:{0}".format(os.getpid()))
    process = multiprocessing.Process(target=new_process, args=("主进程参数", ))
    process.start()
    process.join()
    print("主进程执行完毕！")
