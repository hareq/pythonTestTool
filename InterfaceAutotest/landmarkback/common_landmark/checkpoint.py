# -*- coding: UTF-8 -*-
__author__ = 'guyh'
from common.ctrip import loadkeyword, logger
import unittest
import sys
from array import array
from common.trd.httpbase import http
from landmarkback.common_landmark import getdata,geturl
import urllib


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
        db_lat = data[0]
        db_lon = data[1]
        db_type = data[4]
        db_identityid = data[5]
        #db_cityid = data[6]
        db_id = data[3]

        url = geturl.geturl(db_cityname,db_keyword)  #此处需要替换
        #log.info(url)
        content = http.getresponse_url(url)


        if total(content) == "0":#测试total的个数
            print "关键字测试","测试total结果错误","测试的keyword为:",db_keyword,"城市为",db_cityname
            # log.info("关键字测试")
            # log.info(db_keyword)
            # log.info(content)

        # if total(content) != "0":
        #     #print "测试total结果正确","测试的keyword为:",db_keyword,"城市为",db_cityname
        #     aaa = 0
        #     for nvalue in name(content):
        #         if nvalue==db_keyword:
        #             aaa = 1
        #         else:
        #             pass
        #
        #     if aaa==0:
        #         print "关键字测试","测试data结果错误","测试的keyword为:",db_keyword,"城市为",db_cityname,"name数据库为:",db_keyword,"返回结果为:",nvalue
        #         # log.info("关键字测试")
        #         # log.info(db_keyword)
        #         # log.info(content)
        #     # if lat(content)==db_lat:
        #     # if lon(content)==db_lon:
        #     # if type(content)==db_type:
        #     # if db_id ==id(content):
        #     # if cityname(content)==db_cityname:
        #     # if identityid(content)==db_identityid:
        #     else:
        #         pass
        #         #print "测试data结果正确"
        else:
            pass
    except:
        pass


def checkout_province(data):
    try:
        #print "开始base url的测试"  #此处需要替换
        db_cityname = array('u', data[7]).tostring()[::2].decode('gbk')
        db_keyword = data[2]
        #db_province = array('u', data[13]).tostring()[::2].decode('gbk')
        db_province = data[13]
        db_lat = data[0]
        db_lon = data[1]
        db_type = data[4]
        db_identityid = data[5]
        #db_cityid = data[6]
        db_id = data[3]

        url = geturl.geturl_province(db_cityname,db_keyword,db_province)#此处需要替换
        #log.info(url)
        content = http.getresponse_url(url[0])

        urlbase = geturl.geturl(db_cityname,db_keyword)  #此处需要替换
        contentbase = http.getresponse_url(urlbase)

        if total(contentbase) != "0":
            if total(content) == "0":#测试total的个数
                print "关键字+省份测试","测试total结果错误","测试的keyword为:",db_keyword,"省份为",db_province,"城市为",db_cityname
                # log.info("关键字+省份测试")
                # log.info(db_keyword)
                # log.info(content)
                #print "测试的url为:",url[0]

            # if total(content) != "0":
            #     #print "测试total结果正确","测试的keyword为:",db_keyword,"城市为",db_cityname
            #     if name(content)[0]!=db_keyword:
            #         pass
            #         #print "关键字+省份测试","测试data结果错误","测试的keyword为:",db_keyword,"城市为",db_cityname,"省份为",db_province,"name数据库为:",db_keyword,"返回结果为:",name(content)[0]
            #         # log.info("关键字+省份测试")
            #         # log.info(db_keyword)
            #         # log.info(content)
            #     # if lat(content)==db_lat:
            #     # if lon(content)==db_lon:
            #     # if type(content)==db_type:
            #     # if db_id ==id(content):
            #     # if cityname(content)==db_cityname:
            #     # if identityid(content)==db_identityid:
            #     else:
            #         pass
            #         #print "测试data结果正确"
            else:
                pass
    except:
        pass


def checkout_city(data):
    try:
        #print "开始base url的测试"  #此处需要替换
        db_cityname = array('u', data[7]).tostring()[::2].decode('gbk')
        db_keyword = data[2]
        db_lat = data[0]
        db_lon = data[1]
        db_type = data[4]
        db_identityid = data[5]
        #db_cityid = data[6]
        db_id = data[3]
        db_province = data[13]

        urlbase = geturl.geturl(db_cityname,db_keyword)  #此处需要替换
        contentbase = http.getresponse_url(urlbase)
        url = geturl.geturl_city(db_cityname,db_keyword,db_province)  #此处需要替换
        #log.info(url)
        content = http.getresponse_url(url[0])

        if total(contentbase) != "0":
            if total(content) == "0":#测试total的个数
                print "关键字+城市测试","测试total结果错误","测试的keyword为:",db_keyword,"城市为",db_cityname
                # log.info("关键字+城市测试")
                # log.info(db_keyword)
                # log.info(content)
                #print "测试的url为:",url[0]

            # if total(content) != "0":
            #     #print "测试total结果正确","测试的keyword为:",db_keyword,"城市为",db_cityname
            #     if name(content)[0]!=db_keyword:
            #         pass
            #         #print "关键字+城市测试","测试data结果错误","测试的keyword为:",db_keyword,"城市为",db_cityname,"name数据库为:",db_keyword,"返回结果为:",name(content)[0]
            #         # log.info("关键字+城市测试")
            #         # log.info(db_keyword)
            #         # log.info(content)
            #     # if lat(content)==db_lat:
            #     # if lon(content)==db_lon:
            #     # if type(content)==db_type:
            #     # if db_id ==id(content):
            #     # if cityname(content)==db_cityname:
            #     # if identityid(content)==db_identityid:
            #     else:
            #         pass
            #         #print "测试data结果正确"
            # else:
            #     pass
        else:
            pass
    except:
        pass

def checkout_district(data):
    try:
        #print "开始checkout_district的测试"  #此处需要替换
        db_cityname = array('u', data[7]).tostring()[::2].decode('gbk')
        db_keyword = data[2]
        db_lat = data[0]
        db_lon = data[1]
        db_type = data[4]
        db_identityid = data[5]
        db_cityid = data[6]
        db_id = data[3]
        db_province = data[13]
        db_district = getdata.get_db_district(db_cityid)

        url = geturl.geturl_district(db_cityname,db_keyword,db_district,db_province)  #此处需要替换
        #log.info(url)
        content = http.getresponse_url(url[0])

        if total(content) == "0":#测试total的个数
            print "关键字+行政区测试","测试total结果错误","测试的keyword为:",db_keyword,"城市为",db_cityname,"行政区为：",db_district
            # log.info("关键字+行政区测试")
            # log.info(db_keyword)
            # log.info(content)
            #print "测试的url为:",url[0]

        # if total(content) != "0":
        #     #print "关键字+行政区测试","测试total结果正确","测试的keyword为:",db_keyword,"城市为",db_cityname,"行政区为",db_district
        #     if name(content)[0]!=db_keyword:
        #         pass
        #         #print "关键字+行政区测试","测试data结果错误","测试的keyword为:",db_keyword,"城市为","行政区为：",db_district,db_cityname,"name数据库为:",db_keyword,"返回结果为:",name(content)[0]
        #         # log.info("关键字+行政区测试")
        #         # log.info(db_keyword)
        #         # log.info(content)
        #     # if lat(content)==db_lat:
        #     # if lon(content)==db_lon:
        #     # if type(content)==db_type:
        #     # if db_id ==id(content):
        #     # if cityname(content)==db_cityname:
        #     # if identityid(content)==db_identityid:
        #     else:
        #         pass
        #         #print "测试data结果正确"
        else:
            pass
    except:
        pass

def checkout_downtown(data):
    try:
        #print "开始base url的测试"  #此处需要替换
        db_cityname = array('u', data[7]).tostring()[::2].decode('gbk')
        db_keyword = data[2]
        db_lat = data[0]
        db_lon = data[1]
        db_type = data[4]
        db_province = data[13]
        db_identityid = data[5]
        db_cityid = data[6]
        db_id = data[3]
        db_downtown = getdata.get_db_downtown(db_cityid)

        url = geturl.geturl_downtown(db_cityname,db_keyword,db_downtown,db_province)  #此处需要替换
        #log.info(url)
        content = http.getresponse_url(url[0])

        if total(content) == "0":#测试total的个数
            print "关键字+商业区测试","测试total结果错误","测试的keyword为:",db_keyword,"城市为",db_cityname,"商业区为：",db_downtown
            # log.info("关键字+商业区测试")
            # log.info(db_keyword)
            # log.info(content)
            #print "测试的url为:",url[0]

        # if total(content) != "0":
        #     #print "测试total结果正确","测试的keyword为:",db_keyword,"城市为",db_cityname
        #     if name(content)[0]!=db_keyword:
        #         pass
        #         #print "关键字+商业区测试","测试data结果错误","测试的keyword为:",db_keyword,"城市为","商业区为：",db_downtown,db_cityname,"name数据库为:",db_keyword,"返回结果为:",name(content)[0]
        #         # log.info("关键字+商业区测试")
        #         # log.info(db_keyword)
        #         # log.info(content)
        #     # if lat(content)==db_lat:
        #     # if lon(content)==db_lon:
        #     # if type(content)==db_type:
        #     # if db_id ==id(content):
        #     # if cityname(content)==db_cityname:
        #     # if identityid(content)==db_identityid:
        #     else:
        #         pass
                #print "测试data结果正确"
    except:
        pass