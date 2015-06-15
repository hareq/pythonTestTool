# -*- coding: UTF-8 -*-
__author__ = 'guyh'
import sys
import urllib

reload(sys)
sys.setdefaultencoding('utf-8')

def geturl(cityname,keyword):
    allkeyword = cityname+'" AND address:"'+keyword
    allkeyword = str(allkeyword)
    allkeyword = urllib.quote(allkeyword)
    url = 'http://10.2.6.81:2210/geolocator/search?source=htlinterface&requestFormat=url&responseFormat=xml&query0=city:"'+allkeyword+'"&section0=1-15&return0=name,lat,lon,type,id,cityname,identityid'
    return url

def geturl_city(cityname,keyword,province):
    if cityname not in keyword and province not in keyword:
        allkeyword = cityname+'" AND address:"'+cityname+keyword
        allkeyword = str(allkeyword)
        allkeyword = urllib.quote(allkeyword)
        url = 'http://10.2.6.81:2210/geolocator/search?source=htlinterface&requestFormat=url&responseFormat=xml&query0=city:"'+allkeyword+'"&section0=1-15&return0=name,lat,lon,type,id,cityname,identityid'
    else:
        allkeyword = cityname+'" AND address:"'+keyword
        allkeyword = str(allkeyword)
        allkeyword = urllib.quote(allkeyword)
        url = 'http://10.2.6.81:2210/geolocator/search?source=htlinterface&requestFormat=url&responseFormat=xml&query0=city:"'+allkeyword+'"&section0=1-15&return0=name,lat,lon,type,id,cityname,identityid'
    return url,allkeyword

def geturl_province(cityname,keyword,province):
    if province not in keyword:
        province = str(province)
        allkeyword = cityname+'" AND address:"'+province+keyword
        allkeyword = str(allkeyword)
        allkeyword = urllib.quote(allkeyword)
        url = 'http://10.2.6.81:2210/geolocator/search?source=htlinterface&requestFormat=url&responseFormat=xml&query0=city:"'+allkeyword+'"&section0=1-15&return0=name,lat,lon,type,id,cityname,identityid'

    else:
        allkeyword = cityname+'" AND address:"'+keyword
        allkeyword = str(allkeyword)
        allkeyword = urllib.quote(allkeyword)
        url = 'http://10.2.6.81:2210/geolocator/search?source=htlinterface&requestFormat=url&responseFormat=xml&query0=city:"'+allkeyword+'"&section0=1-15&return0=name,lat,lon,type,id,cityname,identityid'
    return url,allkeyword

def geturl_district(cityname,keyword,district,province):
    if cityname not in keyword and province not in keyword:
        allkeyword = cityname+'" AND address:"'+district+keyword
        allkeyword = str(allkeyword)
        allkeyword = urllib.quote(allkeyword)
        url = 'http://10.2.6.81:2210/geolocator/search?source=htlinterface&requestFormat=url&responseFormat=xml&query0=city:"'+allkeyword+'"&section0=1-15&return0=name,lat,lon,type,id,cityname,identityid'
    else:
        allkeyword = cityname+'" AND address:"'+keyword
        allkeyword = str(allkeyword)
        allkeyword = urllib.quote(allkeyword)
        url = 'http://10.2.6.81:2210/geolocator/search?source=htlinterface&requestFormat=url&responseFormat=xml&query0=city:"'+allkeyword+'"&section0=1-15&return0=name,lat,lon,type,id,cityname,identityid'

    return url,allkeyword

def geturl_downtown(cityname,keyword,downtown,province):
    if cityname not in keyword and province not in keyword:
        allkeyword = cityname+'" AND address:"'+downtown+keyword
        allkeyword = str(allkeyword)
        allkeyword = urllib.quote(allkeyword)
        url = 'http://10.2.6.81:2210/geolocator/search?source=htlinterface&requestFormat=url&responseFormat=xml&query0=city:"'+allkeyword+'"&section0=1-15&return0=name,lat,lon,type,id,cityname,identityid'
    else:
        allkeyword = cityname+'" AND address:"'+keyword
        allkeyword = str(allkeyword)
        allkeyword = urllib.quote(allkeyword)
        url = 'http://10.2.6.81:2210/geolocator/search?source=htlinterface&requestFormat=url&responseFormat=xml&query0=city:"'+allkeyword+'"&section0=1-15&return0=name,lat,lon,type,id,cityname,identityid'

    return url,allkeyword