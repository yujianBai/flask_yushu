#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: yushu_book.py
@time: 2019/2/22 16:16
"""
from httper import HTTP

class YuShuBook():
    isbn_ulr = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}%count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_ulr.format(isbn)
        print ("url:", url)
        result = HTTP.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, count = 15, start = 0):
        url = cls.keyword_url.format(keyword, count, start)
        result = HTTP.get(url)
        return result
