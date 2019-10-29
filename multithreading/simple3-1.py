# coding: utf-8

import _thread
import time


def print_time(threadname, delay):
    count = 0
    while count < 10:
        time.sleep(delay)
        count += 1
        _thread.allocate_lock()
        print("%s: %s" % (threadname, time.ctime(time.time())))


try:
    _thread.start_new_thread(print_time, ("Thread-1", 2))
    _thread.start_new_thread(print_time, ("Thread-2", 4))
except Exception as ex:
    print("Error: ", ex)

while 1:
    # let cpu take a break
    time.sleep(1)
    pass
