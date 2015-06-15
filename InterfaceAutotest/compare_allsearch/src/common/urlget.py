# -*- coding: UTF-8 -*-
__author__ = 'guyh'
import yaml
import os
from common.trd import read_excel


def urlget(testobj):
    nowcmd = os.getcwd()
    #print nowcmd
    f = file('config/cfg_allsearch/url_config.yaml','r')
    return yaml.load(f)[testobj]

def urlall(url,keyword):
    url = url + "&keyword=keywordvlue&districtid=2&lon=121.35801673&lat=31.22016018"
    url = str(url).replace("keywordvlue",keyword)
    return url

def urlall_with_lonlat(url,keyword):
    urllist = []
    file = 'config/cfg_allsearch/url_config.yaml','r'
    data = read_excel.open_excel(file)
    table = data.sheet_by_name("districtid_lon_lat")
    urlnew1 = url + "&keyword=keywordvlue&districtid=2"  #url不带经纬度
    urlnew1 = str(urlnew1).replace("keywordvlue",keyword)
    urllist.append(urlnew1)
    urlnew2 = url + "&keyword=keywordvlue"  #url不带经纬度，不带districtid
    urlnew2 = str(urlnew2).replace("keywordvlue",keyword)
    urllist.append(urlnew2)

    for row_date in range(1, read_excel.rownum(file,"districtid_lon_lat")):  #url带经纬度，带districtid，每次传不同的经纬度，值在excel中取
        districtid = table.cell(row_date, read_excel.find_colum(file,"districtid_lon_lat",'districtid')).value
        lon = table.cell(row_date, read_excel.find_colum(file,"districtid_lon_lat",'lon')).value
        lat = table.cell(row_date, read_excel.find_colum(file,"districtid_lon_lat",'lat')).value
        urlnew = url + "&keyword=keywordvlue&districtid=districtidvalue&lon=lonvalue&lat=latvalue"
        urlnew = str(urlnew).replace("keywordvlue",keyword)
        urlnew = str(urlnew).replace("districtidvalue",districtid)
        urlnew = str(urlnew).replace("lonvalue",lon)
        urlnew = str(urlnew).replace("latvalue",lat)
        urllist.append(urlnew)
    return urllist