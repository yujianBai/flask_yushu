#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: test3.py
@time: 2019/2/26 15:59
"""

import threading

def add(b):
    print(b)
    return b

para = ['10', '11', '12']
thread_list = []

for item in para:
    # print(item)
    t = threading.Thread(target=add, args=(item,))
    thread_list.append(t)

for t in thread_list:
    t.start()
