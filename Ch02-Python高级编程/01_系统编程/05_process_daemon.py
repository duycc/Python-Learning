import multiprocessing
import time


def task():
    for _ in range(10):
        print("[task] running...")
        time.sleep(0.2)


if __name__ == "__main__":
    """
    主进程会等待所有的子进程执行结束再结束
    如果想要主进程退出子进程销毁，可以设置守护主进程或者在主进程退出之前让子进程销毁
    """
    sub_process = multiprocessing.Process(target=task)
    # sub_process.daemon = True
    sub_process.start()

    time.sleep(0.5)
    print("[main] end...")
    # sub_process.terminate()
    exit()
