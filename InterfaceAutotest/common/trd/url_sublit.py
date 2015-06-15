# -*- coding: UTF-8 -*-
__author__ = 'guyh'
import re

def url_ipport_and_vlue(url):
    ipport = re.findall(r"(?<=http://).*?(?=/)",url,re.DOTALL)[0]
    vlue = url.split(ipport)[1]
    return ipport,vlue


def url_split_limitprice(url):
    a = str(re.findall(r"(?<=<limitprice>).*?(?=</)",url,re.DOTALL)[0])
    return a

def url_split_commentscore(url):
    a = str(re.findall(r"(?<=<commentscore>).*?(?=</)",url,re.DOTALL)[0])
    return a

def url_split_zonename(url):
    a = str(re.findall(r"(?<=<zonename>).*?(?=</)",url,re.DOTALL)[0])
    return a

def strfin_between(str,a,b):
    print 11

#print url_ip("http://vacations.ctrip.com/around/p2712188s0.html")