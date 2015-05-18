# -*- coding: UTF-8 -*-
__author__ = 'guyh'

import sys
import urllib

from Framework.trd import read_excel
from Framework.httpbase import http


def start():
    row_date = 1
    andf = 1
    fromt = 1
    andm = 1
    tot =1
    bb = ''

    file = 'D:\work\code\ctriptest\datebase1.xls'
    data = read_excel.open_excel(file)
    table = data.sheet_by_name('type')
    typelist = []
    for row_date in range(1, read_excel.rownum(file,'type')):
        bb = table.cell(row_date, read_excel.find_colum(file,'type','keyword')).value
        #bb = 'shanghai'
        reload(sys)
        sys.setdefaultencoding('utf-8')
        bb = str(bb)
        #time.sleep(2)
        aa = urllib.quote(bb)
        url = 'http://10.2.25.24:8180/appautocomplete/search?keyword='+aa+'&action=autocomplete&source=globalapp63&lon=121.35801673&lat=31.22016018&districtid=2'
        lennum = http.lendate(url)
        num = 0
        for num in range(lennum):
            #print http.get_key_vlue(url,num,"type")
            if http.get_key_vlue(url,num,"type") not in typelist:
                typelist.append(http.get_key_vlue(url,num,"type"))
                print http.get_key_vlue(url,num,"word"), http.get_key_vlue(url,num,"type")

start()
