# coding: utf-8
"""
threading 创建线程简单使用
"""
import threading
import time


class MyThread(threading.Thread):
    thread_id = 0

    def __init__(self, thread_id, name, counter):
        __thread_id = None
        threading.Thread.__init__(self)  # 调用父类初始化
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self) -> None:
        print("starting %s ID [%s]" % (self.name, self.thread_id))
        print_time(self.name, 3, self.counter)
        print("exiting %s ID[%s]" % (self.name, self.thread_id))


def print_time(thread_name, delay, counter):
    while counter:  # 计数器,执行完后自减
        time.sleep(delay)
        print("%s: %s" % (thread_name, time.ctime(time.time())))
        counter -= 1


thread1 = MyThread(1, "thread-1", 1)
thread2 = MyThread(2, "thread-2", 2)

thread1.start()
thread2.start()

print("Main end...")  # Main线程提前结束
