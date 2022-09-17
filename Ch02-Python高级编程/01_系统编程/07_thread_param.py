import time
import threading


def task(count):
    for _ in range(count):
        print("[task] running...")
        time.sleep(0.2)
    else:
        print("[task] end...")


if __name__ == "__main__":
    # sub_thread = threading.Thread(target=task, args=(5,))
    sub_thread = threading.Thread(target=task, kwargs={"count": 5})

    sub_thread.start()
