import time
import threading

def get_data_from_db():
    print("current thread name:{}".format(threading.current_thread().name))
    for i in range(5):
        time.sleep(1)
    print("{0} thread is over!".format(threading.current_thread().name))

if __name__ == "__main__":
    print("{0} thread begin".format(threading.current_thread().name))
    thread = threading.Thread(target=get_data_from_db, name="New thread")
    thread.start()
    thread.join()
    print("{0} main thread is over.".format(threading.current_thread().name))
