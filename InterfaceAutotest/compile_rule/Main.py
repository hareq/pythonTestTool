# -*- coding: UTF-8 -*-

__author__ = 'guguyanhua'

import sys
import urllib
import time

from tools.Compile_rule.src import LoadYaml
from testtools.compile.lib.framework.trd import read_excel
from testtools.compile_rule.lib.framework.httpbase import http


def Language_result(bb):

    aa = urllib.quote(bb)
    url1 = 'http://10.8.91.244:8180/appautocomplete/search?keyword='+aa+'&action=autocomplete&source=globalapp65&lon=121.35801673&lat=31.22016018&districtid=2&type=fortest'
    url2 = 'http://10.8.91.241:8180/appautocomplete/search?keyword='+aa+'&action=autocomplete&source=globalapp65&lon=121.35801673&lat=31.22016018&districtid=2&type=fortest'
    jsonone = http.getresponse_url(url1)
    #jsonone = jsonone.replace(" ","")
    jsontwo = http.getresponse_url(url2)
    #jsontwo = jsontwo.replace(" ","")

    rules = LoadYaml.loadYaml()  # list of Rule
    for rule in rules:
        json1 = rule.execute(jsonone)
        json2 = rule.execute(jsontwo)

    if jsonone == jsontwo:
        print bb,"正确"
        return "1",bb
    else:
        print bb,"错误"
        return "0",bb,jsonone,jsontwo



def start():
    file = 'D:\work\code\ctriptest\datebase1.xls'
    data = read_excel.open_excel(file)
    table = data.sheet_by_name('all')
    f = open('ok.txt', 'w')
    f1 = open('no1.txt', 'w')
    f2 = open('no2.txt', 'w')
    f3 = open('no.txt', 'w')
    for row_date in range(1, read_excel.rownum(file,'all')):
        bb = table.cell(row_date, read_excel.find_colum(file,'all','keyword')).value
        reload(sys)
        sys.setdefaultencoding('utf-8')
        bb = str(bb)
        result = Language_result(bb)
        time.sleep(1)
        if result[0] == "1":
            f.write(result[1])
            f.write("\n")
        else:
            f1.write("############################################")
            f1.write("\n")
            f1.write(result[1])
            f1.write("\n")
            f1.write("############################################")
            f1.write("\n")
            f1.write(result[2].replace(",","\n"))
            f1.write("\n")

            f2.write("############################################")
            f2.write("\n")
            f2.write(result[1])
            f2.write("\n")
            f2.write("############################################")
            f2.write("\n")
            f2.write(result[3].replace(",","\n"))
            f2.write("\n")

            f3.write(result[1])
            f3.write("\n")

    f.close()
    f1.close()
    f2.close()
    f3.close()

start()







