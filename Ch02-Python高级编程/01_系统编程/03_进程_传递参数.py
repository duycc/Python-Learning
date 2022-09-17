import multiprocessing


def task(count):
    for i in range(count):
        print("[task] running...")
    else:
        print("[task] finished...")


if __name__ == "__main__":
    """
    进程传参：
        * 元组方式
        * 字典方式
    """
    # sub_task = multiprocessing.Process(target=task, args=(5,))
    sub_task = multiprocessing.Process(target=task, kwargs={"count": 3})
    sub_task.start()
