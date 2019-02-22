#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: http.py
@time: 2019/2/22 15:57
"""
'''
urllib

requests
'''
import requests

class HTTP:

    @staticmethod
    def get(self, url, return_json=True):
        r = requests.get(url)
        if r.status_code == 200:
            return r.json() if return_json else r.text
        return {} if return_json else ""

