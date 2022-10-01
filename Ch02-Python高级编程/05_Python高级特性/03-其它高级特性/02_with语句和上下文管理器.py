# -*- coding: utf-8 -*-

from contextlib import contextmanager


class File:
    def __init__(self, file_name, file_mode) -> None:
        self.file_name = file_name
        self.file_mode = file_mode

    def __enter__(self):
        print("__enter__")
        self.file = open(self.file_name, self.file_mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")
        self.file.close()


@contextmanager
def d_open(path, mode):
    try:
        file = open(path, mode)
        yield file
    except Exception as e:
        print(e)
    finally:
        print("finally")
        file.close()


def main():
    with File("1.txt", "r") as file:
        file_data = file.read()
        print(file_data)

    with d_open("1.txt", "w") as f:
        f.write("hello, this is contextmanager")


if __name__ == "__main__":
    main()
