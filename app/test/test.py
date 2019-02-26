#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: test.py
@time: 2019/2/26 12:01
"""

from flask import Flask, current_app



app = Flask(__name__)
# app.run()
#应用上下文
#请求上下文

#Flask AppContext
#Request RequestContext

#离线应用/单元测试 //提示 RuntimeError: Working outside of application context. 需主动推入栈

# ctx = app.app_context()
# ctx.push()
# a = current_app
# d = current_app.confg['DEBUG']
# ctx.pop()

with app.app_context():
    a = current_app
    d = current_app.confg['DEBUG']
'''
def __enter__()

def __exit__()

定义一个上下文管理器， 需要实现__enter__, __exit__ (上下文协议)
上下文表达式， 需要返回一个上下文管理器


使用with 的场景：
    open()文件
    数据库的访问
'''

#这段代码报错是因为，current_app context栈顶没有元素，需要手动给appcontext中推入falsk 核心对象,
#flask 默认情况下不需要这么操作是因为， falsk 代码默认在一次request中 主动将flask核心对象推入app_context()中

class A:
    def __enter__(self):
        return self


    def self_func(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("bye")

        # exit方法返回值只能是 True/ False
        # 这个返回值决定whti语句是否抛出异常，
        # 返回True, with不会有异常

with A() as obj_a: #这里的obj_a是 __enter__方法的返回值
    obj_a.self_func()
