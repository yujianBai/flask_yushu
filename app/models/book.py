#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: bool.py
@time: 2019/2/26 10:00
"""

# sqlalchemy
# Flask_SQLAlchemy

from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    id = Column(Integer, primary_key = True, nullable = False)
    title = Column(String(50), nullable = False)
    author = Column(String(30), default='未名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(15), nullable=False, unique=True)
    image = Column(String(50))
    # MVC M model 只有数据 = 数据表
    #ORM 对象关系映射 code first
