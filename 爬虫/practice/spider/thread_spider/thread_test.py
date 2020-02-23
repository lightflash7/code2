# 要点：创建运行子线程，join方法，setDeamon方法
import threading
import time


# 这里用继承Thread类的方法
class sleep_thread(threading.Thread):
    def __init__(self, sleep_time):
        super().__init__()
        self.sleep_time = sleep_time

    def run(self):
        print("sleep for {} seconds start".format(self.sleep_time))
        time.sleep(self.sleep_time)
        print("sleep for {} seconds end".format(self.sleep_time))


if __name__ == '__main__':
    # 当开启一个程序时会默认启动一个线程，叫主线程,即main里面的程序这个线程
    time_start = time.time()
    sleep_2 = sleep_thread(2)
    sleep_3 = sleep_thread(3)
    # 如何使主线程结束关闭别的线程————将别的线程设置为守护线程，用setDaemon()方法
    sleep_2.setDaemon(True)
    sleep_3.setDaemon(True)

    # 用start启动线程
    sleep_2.start()
    sleep_3.start()

    # 如何使得主线程在别的线程执行完再执行————用join()方法
    sleep_2.join()
    sleep_3.join()
    time_end = time.time()

    print(str(time_end - time_start))
