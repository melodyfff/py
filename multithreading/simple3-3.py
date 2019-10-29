# coding: utf-8
"""
threading 线程锁
"""
import threading
import time

thread_lock = threading.RLock()  # 线程锁对象
threads = []  # 线程组


class LockThread(threading.Thread):
    thread_id = 0

    def __init__(self, thread_id, name, counter):
        __thread_id = None
        threading.Thread.__init__(self)  # 调用父类初始化
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self) -> None:
        print("starting %s ID [%s]" % (self.name, self.thread_id))
        thread_lock.acquire()  # 获取锁
        print_time(self.name, 3, self.counter)  # 保证同一时间只有一个线程在执行该函数
        thread_lock.release()  # 释放锁
        print("exiting %s ID[%s]" % (self.name, self.thread_id))


def print_time(thread_name, delay, counter):
    while counter:  # 计数器,执行完后自减
        time.sleep(delay)
        print("%s: %s" % (thread_name, time.ctime(time.time())))
        counter -= 1


thread1 = LockThread(1, "thread-1", 3)
thread2 = LockThread(2, "thread-2", 5)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)


# for t in threads:  # 等待线程完成
#     t.join()

print("Main end...")  # Main线程提前结束
