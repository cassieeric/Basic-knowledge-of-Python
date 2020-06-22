from multiprocessing import Process, Queue
import time

data = []
def set_data(q):
    file = open("1.txt", encoding="utf-8")
    for line in file:
        if "(734615061)" in line:
            q.put(1)
            time.sleep(1)

def get_data(q):
    count = 0
    while True:
        value = q.get(True)
        count += value
        print("The line is : ", count)

if __name__ == '__main__':
    queue = Queue()
    process1 = Process(target=set_data, args=(queue, ))
    process2 = Process(target=get_data, args=(queue, ))
    process1.start()
    process2.start()
    process1.join()

