#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: book.py
@time: 2019/2/25 9:42
"""
from flask import jsonify, request

from app.libs.helper import is_isbn_or_key
from app.forms.book import SearchForm
from app.spider.yushu_book import YuShuBook

from . import web

@web.route("/hello", methods = ["GET"])
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
# app.add_url_rule('/hello', view_func=hello, endpoint=)
#当不传endpoint时， endpiint指向的就是 view_func
# 指定路由的另一种方式
# 基于类的试图（即插视图）

@web.route('/book/search', methods = ["GET"])
def search():
    '''
    http://localhost:9999/web/book/search/9787501524044/0

    t.yushu.im/v2/book/search?q={}&start={}&count={}
    t.yushu.im/v2/book/book/isbn/}{isbn}
    '''
    # q = request.args['q']
    # page = request.args['page']
    #验证参数， 验证层 flask.wtform

    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)

        #reutrn json.dump(result), 200, {'content-type':aplication-json}
        return jsonify(result)
    return jsonify({"msg":form.errors})

