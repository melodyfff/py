#!/usr/bin/python
# -*- coding: UTF-8 -*-
import redis
import urllib.request
import re


def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0')
    response = urllib.request.urlopen(url, timeout=10)
    print(response.info())
    html = response.read()
    return html


def connect():
    pool = redis.ConnectionPool(host='127.0.0.1', port='6379')
    r = redis.Redis(connection_pool=pool)
    return r


def save_re(dataName, data):
    sr = connect()
    sr.set(dataName, data)
    print('save successed!')


def get_re(dataName):
    gr = connect()
    return gr.get(dataName)


# save_re('nov', page)
# search = get_re('nov')
# print(search == None)
print(connect().info())


print('OK')
