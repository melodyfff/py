#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import urllib
import re

def getHtml(url):
	html = urllib.urlopen(url)
	page = html.read()
	return page

def getImg(html):
	reg = r'(<[^>]+>)'
	img = re.compile(reg)
	imglist = re.findall(img,html)
	return imglist


html = getHtml("http://tt.mop.com/16254764.html")
# with open('page.html','wb') as of:
# 	of.write(html)
# print html
list = getImg(html)
print list



print 'done'