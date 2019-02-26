#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: fisher.py
@time: 2019/2/22 14:44
"""

from app import create_app


# 这里需要一个模块的路径
# app.config.from_object 获取的配置， 必须是大写, 所有的配置文件是大写的

from app.web import book
if __name__ == "__main__":
    app = create_app()
    print("appid 启动:", id(app))

    #生产环境部署网络服务器 nginx + uwsgi
    '''
    不会使用 flask 服务器。这个文件时作为一个模块导入到生产环境的
    如果没有这个if __name__ 判断， 在导入时，flask的web服务器就直接运行了 
    '''
    # print(app.url_map)
    # flask中注册的路由将被放到这个 url_map中
    app.run(debug = app.config["DEBUG"], host = '0.0.0.0', port = 9999)




