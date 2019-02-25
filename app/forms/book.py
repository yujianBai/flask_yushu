#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: book.py
@time: 2019/2/25 11:05
"""
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired

class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min = 1, max = 25)]) # DataRequired 防止空格
    page = IntegerField(validators=[NumberRange(min = 1, max = 99)], default=1)
