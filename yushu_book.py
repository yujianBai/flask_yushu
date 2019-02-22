#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: yushu_book.py
@time: 2019/2/22 16:16
"""
from httper import HTTP

class YuShuBook:
    isbn_ulr = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}%count={}&start={}'

    @staticmethod
    def search_by_isbn(self, isbn):
        url = YuShuBook.isbn_ulr.format(isbn)
        result = HTTP.get(url)
        return result

    @staticmethod
    def search_by_keyword(self, keyword, count = 15, start = 0):
        url = YuShuBook.keyword_url.format(keyword, count, start)
        result = HTTP.get(url)
        return result
