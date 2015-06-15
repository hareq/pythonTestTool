# -*- coding: UTF-8 -*-
__author__ = 'guyh'
import httplib

#连接服务器

conn=httplib.HTTPConnection('tuan.ctrip.com')

#发送HTTP请求

conn.request('GET','/nanjing')

#得到结果

result=conn.getresponse()

#获取HTTP请求结果值。200为成功

resultStatus=result.status
print resultStatus

#获取请求的页面内容

content=result.read()

#关闭连接

conn.close()