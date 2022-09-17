import multiprocessing
import time


def dance():
    for i in range(3):
        print("dance...")
        time.sleep(0.2)


def sing():
    for i in range(3):
        print("sing...")
        time.sleep(0.2)


# group: must is None
# name: 进程名
dance_process = multiprocessing.Process(target=dance)
sing_process = multiprocessing.Process(target=sing)


"""
1. 进程执行是无序的
"""
dance_process.start()
sing_process.start()
