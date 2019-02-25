#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: __init__.py.py
@time: 2019/2/25 9:42
"""
from flask import Flask

def create_app():
    app = Flask(__name__)
    print("appid 注册:", id(app))
    app.config.from_object('config')
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
