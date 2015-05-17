# -*- coding: UTF-8 -*-
__author__ = 'guyh'
from base.trd import yamltool

def urlbase():
    return yamltool.dataMap()["url"]["url"]

def url_keyword(keyword):
    url = urlbase()
    url = url.replace("ipvlue",str(yamltool.dataMap()['urlvlue']['ipvlue']))
    url = url.replace("bodyvlue",str(yamltool.dataMap()['urlvlue']['bodyvlue']))
    url = url.replace("actionvlue",str(yamltool.dataMap()['urlvlue']['actionvlue']))
    url = url.replace("lonvlue",str(yamltool.dataMap()['urlvlue']['lonvlue']))
    url = url.replace("latvlue",str(yamltool.dataMap()['urlvlue']['latvlue']))
    url = url.replace("districtidvlue",str(yamltool.dataMap()['urlvlue']['districtidvlue']))
    url = url.replace("sourcevlue",str(yamltool.dataMap()['urlvlue']['sourcevlue']))
    url = url.replace("keywordvlue",keyword)
    return url


def url_ip(ip,keyword):
    url = urlbase()
    url = url.replace("bodyvlue",str(yamltool.dataMap()['urlvlue']['bodyvlue']))
    url = url.replace("ipvlue",ip)
    url = url.replace("actionvlue",str(yamltool.dataMap()['urlvlue']['actionvlue']))
    url = url.replace("lonvlue",str(yamltool.dataMap()['urlvlue']['lonvlue']))
    url = url.replace("latvlue",str(yamltool.dataMap()['urlvlue']['latvlue']))
    url = url.replace("districtidvlue",str(yamltool.dataMap()['urlvlue']['districtidvlue']))
    url = url.replace("sourcevlue",str(yamltool.dataMap()['urlvlue']['sourcevlue']))
    url = url.replace("keywordvlue",keyword)
    return url

def url_sourc(source,keyword):
    url = urlbase()
    url = url.replace("ipvlue",str(yamltool.dataMap()['urlvlue']['ipvlue']))
    url = url.replace("bodyvlue",str(yamltool.dataMap()['urlvlue']['bodyvlue']))
    url = url.replace("actionvlue",str(yamltool.dataMap()['urlvlue']['actionvlue']))
    url = url.replace("lonvlue",str(yamltool.dataMap()['urlvlue']['lonvlue']))
    url = url.replace("latvlue",str(yamltool.dataMap()['urlvlue']['latvlue']))
    url = url.replace("districtidvlue",str(yamltool.dataMap()['urlvlue']['districtidvlue']))
    url = url.replace("sourcevlue",source)
    url = url.replace("keywordvlue",keyword)
    return url

def ipcompile():
    return yamltool.dataMap()["urlcompile"]["ipcompile"]

def ipvlue():
    return yamltool.dataMap()["urlvlue"]["ipvlue"]

def sourcecompile():
    return yamltool.dataMap()["urlcompile"]["sourcecompile"]

def sourcevlue():
    return yamltool.dataMap()["urlvlue"]["sourcevlue"]
