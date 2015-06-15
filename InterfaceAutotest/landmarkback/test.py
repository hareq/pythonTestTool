# -*- coding: UTF-8 -*-
__author__ = 'guyh'

import sys
from array import array
from common.trd.httpbase import http
from landmark.common_landmark import getdata,geturl
import urllib
#
# url = 'http://10.2.6.81:2210/geolocator/search?source=htlinterface&requestFormat=url&responseFormat=xml&query0=city:"shenyang" AND keyword:"shenyangzhan"&section0=1-15'
# content = http.getresponse_url(url)
# #print content

def GetMiddleStrlist(content,startStr,endStr):
    n = 0
    strlist = []
    while n <= len(content):
        if content.find(startStr,n) > 0:
            n = content.find(startStr,n)
            startIndex = n
            print "startIndex",startIndex
            if startIndex >= 0:
                startIndex += len(startStr)
                endIndex = content.index(endStr,n)
                print "endIndex",endIndex
                strlist.append(content[startIndex:endIndex])
                n = n+1
        else:
            n = n+1
    return strlist

aa = """
<?xml version="1.0" encoding="UTF-8"?>
<Responses>
    <Response>
        <ServerIP>10.2.6.81</ServerIP>
        <total>3</total>
        <time>1</time>
        <result>
            <doc>
                <name>芝山站?</name>
                <lat>25.10306</lat>
                <lon>121.522514</lon>
                <type>markland</type>
                <id>4214399</id>
                <cityname>台北</cityname>
                <identityid>markland_4214399</identityid>
            </doc>
            <doc>
                <name>芝山站</name>
                <lat>25.10306</lat>
                <lon>121.522514</lon>
                <type>markland</type>
                <id>4214486</id>
                <cityname>台北</cityname>
                <identityid>markland_4214486</identityid>
            </doc>
            <doc>
                <name>芝山站</name>
                <lat>25.103059</lat>
                <lon>121.522513</lon>
                <type>metrostation</type>
                <id>2971</id>
                <cityname>台北</cityname>
                <identityid>metrostation_2971</identityid>
            </doc>
        </result>
    </Response>
</Responses>
"""
for n in GetMiddleStrlist(aa,"<name>","</name>"):
    print n