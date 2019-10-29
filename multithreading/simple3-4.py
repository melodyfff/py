# coding: utf-8
"""
Queue 线程队列的使用
Queue自带阻塞,当队列满的时候再put(),当前put()操作线程会进入阻塞,直到队列被消耗
"""
import queue
import threading
import time

EXIT_FLAG = 0

threads = []  # 线程组

queue_lock = threading.Lock()  # 队列锁对象
work_queue = queue.Queue(3)  # 初始化队列 LifoQueue

data_list = ['1', '2', '3', '4', '5']  # 队列数据


class QueueThread(threading.Thread):
    thread_id = None
    q = None

    def __init__(self, thread_id, name, q):
        __thread_id = None
        threading.Thread.__init__(self)  # 调用父类初始化
        self.thread_id = thread_id
        self.name = name
        self.q = q

    def run(self) -> None:
        print("starting %s ID [%s]" % (self.name, self.thread_id))
        process_data(self.name, self.q)
        print("exiting %s ID[%s]" % (self.name, self.thread_id))


def process_data(thread_name, q):
    while not EXIT_FLAG:
        queue_lock.acquire()  # 获取锁
        if not work_queue.empty():
            out = q.get()
            print(">>> %s processing %s" % (thread_name, out))
        queue_lock.release()  # 释放锁
        time.sleep(1)  # take cpu release


for i in range(1, 10):
    thread = QueueThread(i, '{}-{}'.format('thread', i), work_queue)  # 创建线程
    thread.start()

# queue_lock.acquire()  # Main线程获取锁填充数据
for data in data_list:  # 填充数据
    time.sleep(0.02)
    work_queue.put(data)  # 这里如果队列满了会进入等待,除非被消耗,否则当前线程进行等待 ,timeout参数设置超时时间,如果时间到了还未入队,则抛出队列full异常
# queue_lock.release()  # Main线程释放锁

while not work_queue.empty():  # 等待队列清空
    pass

EXIT_FLAG = 1  # 标记线程可以结束

print("Main end...")  # Main线程提前结束
