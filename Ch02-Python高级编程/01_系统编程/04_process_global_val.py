import multiprocessing


g_list = list()


def add_data():
    global g_list
    for i in range(5):
        g_list.append(i)
    print("[add_data] g_list={}".format(g_list))


def read_data():
    global g_list
    print("[read_data] g_list={}".format(g_list))


def main():
    """
    创建子进程会对主进程资源进行拷贝，也就是说子进程是主进程的一个副本，好比是一对双胞胎，之所以进程之间不共享全局变量，
    是因为操作的不是同一个进程里面的全局变量，只不过不同进程里面的全局变量名字相同而已。
    """
    add_data_process = multiprocessing.Process(target=add_data)
    read_data_process = multiprocessing.Process(target=read_data)

    add_data_process.start()
    add_data_process.join()

    read_data_process.start()

    print("[main] g_list={}".format(g_list))


if __name__ == "__main__":
    main()
