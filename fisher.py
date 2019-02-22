#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: fisher.py
@time: 2019/2/22 14:44
"""

from flask import Flask, make_response, jsonify

from helper import is_isbn_or_key
from yushu_book import YuShuBook

app = Flask(__name__)

app.config.from_object('config')
# 这里需要一个模块的路径
# app.config.from_object 获取的配置， 必须是大写, 所有的配置文件是大写的

@app.route("/hello", methods = ["GET"])
def hello():
    # return "hello"

    headers = {
       'content-type':'text/plain', # 浏览器会根据content-type 的格式，分析返回值
       #'content-type':'applicaton/json', //返回json 格式的数据
       'localtion':'http://www.baidu.com',
    }
    #response = make_response('<html></html>', 301)
    #response.headers = headers
    #return response

    return '<html></html>', 301, headers
#视图函数的return flask 在后边做了封装,并不是简简单单的 'hello'
#status code 200, 404, 301
#content-type http headers // 告诉浏览器服务器返回的数据是什么


# app.add_url_rule('/hello', view_func=hello)
# 指定路由的另一种方式
# 基于类的试图（即插视图）


@app.route('/book/search/<q>/<page>', methods = ["GET"])
def search(q, page):
    '''
    t.yushu.im/v2/book/search?q={}&start={}&count={}
    t.yushu.im/v2/book/book/isbn/}{isbn}

    q
    start
    count
    isbn
    :return:
    '''

    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)

    return jsonify(result)

if __name__ == "__main__":
    #生产环境部署网络服务器 nginx + uwsgi
    '''
    不会使用 flask 服务器。这个文件时作为一个模块导入到生产环境的
    如果没有这个if __name__ 判断， 在导入时，flask的web服务器就直接运行了 
    '''
    app.run(debug = app.config["DEBUG"], host = '0.0.0.0', port = 9999)


