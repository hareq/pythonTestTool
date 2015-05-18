# -*- coding: UTF-8 -*-
__author__ = 'guyh'

#######################################################################################################################################
# send_get_result(ipport,url)--发出的get返回的响应全部内容，参数ipport例子：'10.8.119.200:8180'，参数url例子：appautocomplete/search?keyword=东方明珠&action=autocomplete&source=globalapp63&lon=121.35801673&lat=31.22016018&districtid=2


import httplib
import json

from Framework.trd import url_sublit


def HttpSendRequest(url):
    ipport = url_sublit.url_ipport_and_vlue(url)[0]
    vlue = url_sublit.url_ipport_and_vlue(url)[1]
    conn = httplib.HTTPConnection(ipport)
    conn.request(method="get",url=vlue)
    return conn

def getresponse(conn):
    result = conn.getresponse()
    content = result.read()
    return content

###############################
#下面的方法是每次都传入url，每个方法都执行一次HttpSendRequest
def getresponse_url(url):
    result = HttpSendRequest(url).getresponse()
    content = result.read()
    return content

def getresponse_url_python(url):
    result = HttpSendRequest(url).getresponse()
    content = result.read()
    content = json_to_py(content)
    return content

def getresponse_getheaders_url(url):
    result = HttpSendRequest(url).getresponse().getheaders()
    #content = result.read()
    return result

def getresponse_headauth_url(url):
    vlue = getresponse_url(url)
    ipport = url_sublit.url_ipport_and_vlue(vlue)


#此方法将json转换为python格式
def json_to_py(jsonvlue):
    jsonvlue = json.loads(jsonvlue)
    return jsonvlue

#输入head里的auth或者errcode，返回他们的值
def head(url,key):
    a = getresponse_url(url)
    a = json_to_py(a)
    vlue = str(key)
    return a["head"][vlue]

#date的个数
def lendate(url):
    a = getresponse_url(url)
    a = json_to_py(a)
    return len(a["data"])

def vluecount(url,Key,vlue):
    a = getresponse_url(url)
    a = json_to_py(a)
    n = 0
    for i in range(0, lendate(url)):
        if a["data"][i][Key] == vlue:
            n = n+1
    return n-1

#通过传入url，date的列表键值，key，获得key所对应的值
def get_key_vlue(url,num,key):
    a = getresponse_url(url)
    a = json_to_py(a)
    num = int(num)
    return a["data"][num][key]

#通过传入url，word值，和键值，得到该word对应的键值，比如word传入上海，键值传入type，得出上海的type值
def get_vlue_use_word(urlvlue,key1,keyword,key2):
    num = vluecount(urlvlue,key1,keyword)
    return get_key_vlue(urlvlue,num,key2)


