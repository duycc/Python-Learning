import multiprocessing
import os
import time


def dance():
    print("[dance] pid={} ppid={} name={}".format(os.getpid(), os.getppid(), multiprocessing.current_process()))
    for i in range(3):
        print("dance...")
        time.sleep(0.2)
        os.kill(os.getpid(), 9)


def sing():
    print("[sing] pid={} name={}".format(os.getpid(), multiprocessing.current_process()))
    for i in range(3):
        print("sing...")
        time.sleep(0.2)


# group: must is None
# name: 进程名
dance_process = multiprocessing.Process(target=dance)
sing_process = multiprocessing.Process(target=sing)


if __name__ == "__main__":
    """
    进程执行是无序的
    """
    print("[main] pid={} name={}".format(os.getpid(), multiprocessing.current_process()))
    dance_process.start()
    sing_process.start()
