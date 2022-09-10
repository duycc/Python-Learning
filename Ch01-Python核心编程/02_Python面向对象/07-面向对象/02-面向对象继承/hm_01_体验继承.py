class A:
    def __init__(self) -> None:
        self.num = 1

    def print_info(self):
        print(self.num)


class B(A):
    pass


result = B()
result.print_info()
