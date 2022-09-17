import time
import threading


def dance():
    for _ in range(3):
        print("[dance] running...")
        time.sleep(1)


def sing():
    for _ in range(3):
        print("[sing] running")
        time.sleep(1)


if __name__ == "__main__":
    dance_thread = threading.Thread(target=dance)
    sing_thread = threading.Thread(target=sing)

    dance_thread.start()
    sing_thread.start()
