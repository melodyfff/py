#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import re

line = '<img src="http://i1.mopimg.cn/img/tt/2016-12/215/20161230173134351.jpg790x600.jpg">'

matchObj = re.search(r'((?:http|https)(?::\\/{2}[\\w]+)(?:[\\/|\\.]?)(?:[^\\s"]*))',line,re.M|re.I)

if matchObj:
	print matchObj.group()
else:
	print 'No match'

img = re.compile(r"<img src='(.*?)'")
imglist = re.findall(img,line)
print imglist

