#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: __init__.py.py
@time: 2019/2/25 9:42
"""
from flask import Flask

from app.models.book import db


def create_app():
    app = Flask(__name__)
    print("appid 注册:", id(app))
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    db.init_app(app)
    db.create_all(app = app)
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
