#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: user.py
@time: 2019/2/25 10:41
"""
from . import web

@web.route('/url', methods = ['GET'])
def login():
    pass