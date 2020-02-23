import threading

total = 0
nums = 1000000
total_lock = threading.Lock()


def add_total():
    global total
    global nums
    for i in range(nums):
        total_lock.acquire()
        total = total + 1
        total_lock.release()


def sub_total():
    global total
    global nums
    for i in range(nums):
        total_lock.acquire()
        total = total - 1
        total_lock.release()


if __name__ == '__main__':
    add_threading = threading.Thread(target=add_total)
    sub_threading = threading.Thread(target=sub_total)
    add_threading.start()
    sub_threading.start()
    # 记得join才是最终输出
    add_threading.join()
    sub_threading.join()
    print(total)