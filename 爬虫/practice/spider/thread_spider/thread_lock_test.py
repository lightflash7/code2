# 运行这一段代码会发现结果并不为0，这就是没有锁保护下的数据问题。
# 不为0的原因就是因为运行进程add_threading的时候又会切到sub_threading，然后还没有赋值就被另一个进程读取了
# 解决方案就是加锁，加锁的代码见thread_lock_test2
import threading

total = 0
nums = 1000000


def add_total():
    global total
    global nums
    for i in range(nums):
        total = total + 1


def sub_total():
    global total
    global nums
    for i in range(nums):
        total = total - 1


if __name__ == '__main__':
    add_threading = threading.Thread(target=add_total)
    sub_threading = threading.Thread(target=sub_total)
    add_threading.start()
    sub_threading.start()
    # 记得join才是最终输出
    add_threading.join()
    sub_threading.join()
    print(total)
