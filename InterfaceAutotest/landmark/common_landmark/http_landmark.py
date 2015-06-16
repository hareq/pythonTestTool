# -*- coding: UTF-8 -*-
__author__ = 'guyh'

#######################################################################################################################################
# send_get_result(ipport,url)--发出的get返回的响应全部内容，参数ipport例子：'10.8.119.200:8180'，参数url例子：appautocomplete/search?keyword=东方明珠&action=autocomplete&source=globalapp63&lon=121.35801673&lat=31.22016018&districtid=2


import httplib
import json
from common.trd import url_sublit


def HttpSendRequest():
    ipport = "10.2.6.81:2210"
    conn = httplib.HTTPConnection(ipport)
    return conn


def getresponse(conn,vlue):
    conn.request('GET',vlue)
    result = conn.getresponse()
    content = result.read()
    return content

