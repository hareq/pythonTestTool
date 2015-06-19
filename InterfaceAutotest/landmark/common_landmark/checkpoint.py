# -*- coding: UTF-8 -*-
__author__ = 'guyh'
from common.ctrip import logger
import sys
from array import array
from common.trd.httpbase import http
from landmark.common_landmark import getdata,geturl


reload(sys)
sys.setdefaultencoding('utf-8')
log = logger.logger()

def GetMiddleStr(content,startStr,endStr):
    startIndex = content.index(startStr)
    if startIndex >= 0:
        startIndex += len(startStr)
        endIndex = content.index(endStr)
    return content[startIndex:endIndex]

def GetMiddleStrlist(content,startStr,endStr):
    startIndex = content.index(startStr)
    if startIndex >= 0:
        startIndex += len(startStr)
        endIndex = content.index(endStr)
    return content[startIndex:endIndex]

def GetMiddleStrlist(content,startStr,endStr):
    n = 0
    strlist = []
    while n <= len(content):
        if content.find(startStr,n) > 0:
            n = content.find(startStr,n)
            startIndex = n
            if startIndex >= 0:
                startIndex += len(startStr)
                endIndex = content.index(endStr,n)
                strlist.append(content[startIndex:endIndex])
                n = n+1
        else:
            n = n+1
    return strlist

def total(content):
    try:
        return GetMiddleStr(content,"<total>","</total>")
    except:
        print "没有找到total",content,

def name(content):
    try:
        return GetMiddleStrlist(content,"<name>","</name>")
    except:
        pass

def lat(content):
    try:
        return GetMiddleStr(content,"<lat>","</lat>")
    except:
        pass

def lon(content):
    try:
        return GetMiddleStr(content,"<lon>","</lon>")
    except:
        pass

def type(content):
    try:
        return GetMiddleStr(content,"<type>","</type>")
    except:
        pass

def id(content):
    try:
        return GetMiddleStr(content,"<id>","</id>")
    except:
        pass

def cityname(content):
    try:
        return GetMiddleStr(content,"<cityname>","</cityname>")
    except:
        pass

def identityid(content):
    try:
        return GetMiddleStr(content,"<identityid>","</identityid>")
    except:
        pass

def checkout_base(data):
    try:
        db_cityname = array('u', data[7]).tostring()[::2].decode('gbk')
        db_keyword = data[2]
        url = geturl.geturl(db_cityname,db_keyword)  #此处需要替换
        #log.info(url)
        content = http.getresponse_url(url)

        if total(content) == "0":#测试total的个数
            print "关键字测试","测试total结果错误","测试的keyword为:",db_keyword,"城市为",db_cityname
        else:
            pass
    except:
        pass


def checkout_province(data):
    try:
        db_cityname = array('u', data[7]).tostring()[::2].decode('gbk')
        db_keyword = data[2]
        db_province = data[13]

        url = geturl.geturl_province(db_cityname,db_keyword,db_province)#此处需要替换
        #log.info(url)
        content = http.getresponse_url(url[0])

        urlbase = geturl.geturl(db_cityname,db_keyword)  #此处需要替换
        contentbase = http.getresponse_url(urlbase)

        if total(contentbase) != "0":
            if total(content) == "0":#测试total的个数
                print "关键字+省份测试","测试total结果错误","测试的keyword为:",db_keyword,"省份为",db_province,"城市为",db_cityname
            else:
                pass
    except:
        pass


def checkout_city(data):
    try:
        db_cityname = array('u', data[7]).tostring()[::2].decode('gbk')
        db_keyword = data[2]
        db_province = data[13]

        urlbase = geturl.geturl(db_cityname,db_keyword)  #此处需要替换
        contentbase = http.getresponse_url(urlbase)
        url = geturl.geturl_city(db_cityname,db_keyword,db_province)  #此处需要替换
        #log.info(url)
        content = http.getresponse_url(url[0])

        if total(contentbase) != "0":
            if total(content) == "0":#测试total的个数
                print "关键字+城市测试","测试total结果错误","测试的keyword为:",db_keyword,"城市为",db_cityname
        else:
            pass
    except:
        pass

def checkout_district(data):
    try:
        db_cityname = array('u', data[7]).tostring()[::2].decode('gbk')
        db_keyword = data[2]
        db_cityid = data[6]
        db_province = data[13]
        db_district = getdata.get_db_district(db_cityid)

        url = geturl.geturl_district(db_cityname,db_keyword,db_district,db_province)  #此处需要替换
        #log.info(url)
        content = http.getresponse_url(url[0])
        #print total(content)

        if total(content) == "0":#测试total的个数
            print "关键字+行政区测试","测试total结果错误","测试的keyword为:",db_keyword,"城市为",db_cityname,"行政区为：",db_district
        else:
            pass
    except:
        pass

def checkout_downtown(data):
    try:
        #print "开始base url的测试"  #此处需要替换
        db_cityname = array('u', data[7]).tostring()[::2].decode('gbk')
        db_keyword = data[2]
        db_province = data[13]
        db_cityid = data[6]
        db_downtown = getdata.get_db_downtown(db_cityid)

        url = geturl.geturl_downtown(db_cityname,db_keyword,db_downtown,db_province)  #此处需要替换
        #log.info(url)
        content = http.getresponse_url(url[0])

        if total(content) == "0":#测试total的个数
            print "关键字+商业区测试","测试total结果错误","测试的keyword为:",db_keyword,"城市为",db_cityname,"商业区为：",db_downtown
    except:
        pass