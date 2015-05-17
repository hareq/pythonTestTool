# -*- coding: utf-8 -*-
__author__ = 'guyh'
from base.trd import read_excel
import sys
import urllib
from base.trd import read_excel
import time
from base.httpbase import http
from ctrip.ctripmethod import testcasedata

###################################################
##测试case，从a-k个用例，每条用例包括测试globalapp63和mobileweb
##测试case，从a-k个用例，每条用例包括测试globalapp63和mobileweb
#a:目的地 ok
#b:保险公司
#c:保险类型
#d:目的地+保险公司
#e:目的地+保险类型
#f:保险公司+保险类型
#g:目的地+保险公司+保险类型

#b:多保险公司
#c:多保险类型
#k:目的地+多保险公司
#h:目的地+多保险类型
#i:多保险类型+多保险公司
#j:目的地+多保险类型+多保险公司


#测试每条case的errcode，word，insurance，url中含的destination，FeatureList，CompanyList个数和值，mobileweb可以测url跳转后值界面的值是否正确
#输出每个globalapp63的url和keyword，用来跳转用

#报告输出格式为：成功
#                失败：关键字+失败的内容+应该的值+目前的值
###################################################
file = testcasedata.RegressionTestDate()
data = read_excel.open_excel(file)
c = "globalapp64"
#c = "mobileweb"
keyword = ''
def test_case_a(data,c):
    keywordvlue = "destination"
    #keywordvlue = "CompanyList"
    #keywordvlue = "FeatureList"
    table = data.sheet_by_name('url')
    urlhttp = table.cell(1,read_excel.find_colum(file,'url','url')).value+"action=autocomplete&source=globalapp64&lon=121.35801673&lat=31.22016018&districtid=2"+"&keyword="+keyword
    for row_date in range(1, read_excel.rownum(file,'insurance')):
        table = data.sheet_by_name('insurance')
        bb = table.cell(row_date,read_excel.find_colum(file,'insurance',keywordvlue)).value
        reload(sys)
        sys.setdefaultencoding('utf-8')
        bb = str(bb)
        aa = urllib.quote(bb)
        urldate = urlhttp+aa+urllib.quote("保险")
        lennum = http.lendate(urldate)
        errcode = http.head(urldate,"errcode")
        word = http.get_key_vlue(urldate,0,"word")
        type = http.get_key_vlue(urldate,0,"type")
        urlt = http.get_key_vlue(urldate,0,"url")
        count = urlt.count(keywordvlue)
        #print lennum,word,bb+"保险",errcode,type,count
        if lennum == 1 and word == bb+"保险" and errcode ==0 and type == "insurance" and count==1:
            print word,urlt
            #print urldate
        else:
            print word,urlt

test_case_a(data,c)
