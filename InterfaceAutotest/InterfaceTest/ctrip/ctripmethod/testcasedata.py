# -*- coding: utf-8 -*-
# coding=gbk
__author__ = 'guyh'

from Framework.trd import xmloperate
from Framework.trd import read_excel, configfile


def RegressionTestDate():
    text = configfile.configfile()
    TagName = "datefile"
    Attribute = "route"
    return xmloperate.getnodeValue(text,TagName,Attribute)

###########################下面的是url页的相关方法
def getiplist():
    file = RegressionTestDate()
    return read_excel.excel_table_byname(file,"url","url")

def getsourcelist():
    file = RegressionTestDate()
    return read_excel.excel_table_byname(file,"url","source")

def keylist():
    file = RegressionTestDate()
    read_excel.excel_table_onecol(file,"url",0)
    return  read_excel.excel_table_onecol(file,"url",0)

#print keylist()
#print getsourcelist()
#print getsourcelist()[2].encode('utf8')

def url():
    print keylist()
    url = ""
    for n in range(1,len(keylist())):
        print keylist()[n]
        url = url+"'"+keylist()[n]+"="+"'"+keylist()[n]+"vlue"+"'"+"+"+"'"+"&"+"'"+"+"
    print "aa","urlvlue+"+url

###########################下面的是各个业务页的key获取方法
def channel_keyword():
    file = RegressionTestDate()
    return read_excel.excel_table_byname(file,"channel","keyword")

def channelplane_keyword():
    file = RegressionTestDate()
    return read_excel.excel_table_byname(file,"channelplane","keyword")

print url()