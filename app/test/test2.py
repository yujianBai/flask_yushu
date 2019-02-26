#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: test2.py
@time: 2019/2/26 15:45
"""

# 更加充分的利用cpu 的性能优势
# 异步编程
# 单核cpu
# 4核， 8核 并行的执行程序
'''
python 不能充分的利用多核cpu的性能
GIL 全局解释器锁：
    锁，是为了线程安全
        细粒度：
            程序员自己加的锁
        粗粒度：        
            GIL  
    内存资源 一个进程有多个线程， 他们之间是共享资源

python 是一门语言， 其中起作用的是cpython jpython 
而GIL是存在 cpython 中的


python 多线程 是不是鸡肋
    对于io 密集型程序，并不是 (主要耗时是等待io 操作返回)
    cpu密集型程序 可以这么认为
'''
import threading

def worker():
    t = threading.current_thread()
    print(t.getName() + 'worker \n')
    print("i am bai")


new_t = threading.Thread(target=worker, name = 'qiyue_thread')
new_t.start()

t = threading.current_thread()
print(t.getName() + 'thread \n')
