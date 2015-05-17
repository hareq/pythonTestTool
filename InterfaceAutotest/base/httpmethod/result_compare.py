# -*- coding: utf-8 -*-
__author__ = 'guyh'

from base.httpbase import http

def compare_result_all(url1,url2):
    if http.getresponse_url(url1) == http.getresponse_url(url2):
        return 1
    else:
        return 0


#print compare_result_all("http://10.8.119.200:8180/appautocomplete/search?keyword=beijing&action=autocomplete&source=globalapp62&lon=121.35801673&lat=31.22016018&districtid=2","http://10.8.119.200:8180/appautocomplete/search?keyword=shanghai&action=autocomplete&source=globalapp64&lon=121.35801673&lat=31.22016018&districtid=2")