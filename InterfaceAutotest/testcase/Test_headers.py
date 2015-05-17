# -*- coding: UTF-8 -*-
__author__ = 'guyh'

import urllib
from base.trd import read_excel
from base.httpbase import http
import unittest
import sys

class Test_headers(unittest.TestCase):
    def headers_ContentType_Test(self):
        error = 0
        file = 'D:\work\code\ctriptest\datebase1.xls'
        data = read_excel.open_excel(file)
        table = data.sheet_by_name('all')
        for row_date in range(1,read_excel.rownum(file,'all')):
            bb = table.cell(row_date,read_excel.find_colum(file,'all','keyword')).value
            reload(sys)
            sys.setdefaultencoding('utf-8')
            bb = str(bb)
            aa = urllib.quote(bb)
            url1 = 'http://10.8.91.244:8180/appautocomplete/search?keyword='+aa+'&action=autocomplete&source=globalapp65&lon=121.35801673&lat=31.22016018&districtid=2&type=fortest'
            content = http.getresponse_getheaders_url(url1)
            for n in range(len(content)):
                if content[n][0] == "content-type":
                    if content[n][1] != "application/json; charset=UTF-8":
                        error = error+1
                        print bb,content[n][1]
                    else:
                        print bb,"通过"
        assert error == 0


