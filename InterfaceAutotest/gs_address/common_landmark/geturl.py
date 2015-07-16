# -*- coding: UTF-8 -*-
__author__ = 'guyh'
import sys
import urllib

reload(sys)
sys.setdefaultencoding('utf-8')

def geturl(districtid,keyword):
    # print "start get url"
    # print districtid,keyword
    keyword = str(keyword)
    keyword = urllib.quote(keyword)
    # print 'keyword',keyword
    url = 'http://10.2.25.24:8180/appautocomplete/search?keyword='+keyword+'&action=autocomplete&source=gsapp66&lon=121.534279&lat=31.209871&districtid='+str(districtid)
    # print "url",url
    return url
