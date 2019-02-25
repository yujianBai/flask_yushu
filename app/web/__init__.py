#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: __init__.py.py
@time: 2019/2/25 9:42
"""
from flask import Blueprint
web = Blueprint('web', __name__) # 注册蓝图

from app.web import book
from app.web import user