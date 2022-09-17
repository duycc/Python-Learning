import time
import threading

g_num = 0
num_mutex = threading.Lock()


def add_task():
    global g_num
    num_mutex.acquire()
    for _ in range(1000000):
        g_num += 1
    num_mutex.release()


if __name__ == "__main__":
    t1 = threading.Thread(target=add_task)
    t2 = threading.Thread(target=add_task)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("[main] g_num={}".format(g_num))
