# coding: utf-8
"""
multiprocessing 线程池的用法
"""
from multiprocessing import Pool
import multiprocessing


def test(hello,ok=None):
    print('{} - {}'.format(multiprocessing.current_process(), hello))
    pass


p = Pool(5)

for i in range(100):
    p.apply(func=test, args=tuple(str(i)))

p.close()  # 关闭连接池,不再接收任务
p.join()  # 等待任务执行完毕
