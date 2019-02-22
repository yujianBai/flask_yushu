#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: helper.py
@time: 2019/2/22 15:53
"""

def is_isbn_or_key(word):
    isbn_or_key = "key"
    if len(word) == 13 and word.isdgit():
        isbn_or_key = "isbn"
    if '-' in word and len(word) == 10 and word.replace('-', '').isdgit():
        isbn_or_key = "isbn"
    return isbn_or_key

