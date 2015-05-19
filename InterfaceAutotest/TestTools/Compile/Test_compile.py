# -*- coding: UTF-8 -*-
__author__ = 'guyh'
import sys
import urllib
import time
import json
import re
import sys

from Framework.trd import read_excel
from Framework.httpbase import http


def getpairpattern(regstr):
    temp = regstr.replace("(","SPECIALMARK")
    temp = temp.replace(")","(")
    temp = temp.replace("SPECIALMARK",")")
    temp = "("+temp+")"
    temp = temp.replace("()","")
    return re.compile(temp)


def filteroutsting(src,regstr):
    pattern = re.compile(regstr)
    pairPattern = getpairpattern(regstr)
    stringLeft=src
    result=[]
    matchIterator = pattern.finditer(src)
    for match in matchIterator:
        fullString = match.group(0)
        temp = pairPattern.match(fullString)
        if (temp):
            replaceString="".join(temp.groups())
    # print fullString
    # print replaceString
        stringLeft=stringLeft.replace(fullString,replaceString)
        result.append(match.groups());
        result.append(stringLeft)

    #print result
    return result

def Language_result(bb):
    aa = urllib.quote(bb)
    url1 = 'http://10.2.25.24:8180/appautocomplete/search?keyword='+aa+'&action=autocomplete&source=globalapp65&lon=121.35801673&lat=31.22016018&districtid=2&type=fortest'
    url2 = 'http://10.8.91.241:8180/appautocomplete/search?keyword='+aa+'&action=autocomplete&source=globalapp65&lon=121.35801673&lat=31.22016018&districtid=2&type=fortest'
    #print bb
    content1 = http.getresponse_url(url1)
    content1 = content1.replace(" ","")
    # try:
    #     for n in range(len(json.loads(content1)["data"])):
    #         if json.loads(content1)["data"][n]["type"] == "hotel":
    #             rrr = json.loads(content1)["data"][n].pop("price")
    #             content1 = content1.replace(rrr,"")
    # except Exception:
    #     print Exception

    content2 = http.getresponse_url(url2)
    content2 = content2.replace(" ","")

    print "原",content1
    print "鸣哥" ,filteroutsting(content1,"sdfdf")

    # try:
    #     for m in range(len(json.loads(content2)["data"])):
    #         if json.loads(content2)["data"][m]["type"] == "hotel":
    #             ttt = json.loads(content2)["data"][m].pop("price")
    #             content2 = content2.replace(ttt,"")
    # except Exception:
    #     print Exception

    if content1 == content2:
        #ok.append(bb)
        print bb,"正确"
        return "1",bb
        #1 == 1
    else:
        print bb,"错误"
        return "0",bb,content1,content2
        #no.append(bb)

    # lennum = http.lendate(url1)
    # num = 0
    # for num in range(lennum):
    #     print http.get_key_vlue(url1,num,"word")
    #     print http.get_key_vlue(url1,num,"type")


def start():
    row_date = 1
    andf = 1
    fromt = 1
    andm = 1
    tot =1
    bb = ''

    file = 'config\datebase1.xls'
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
