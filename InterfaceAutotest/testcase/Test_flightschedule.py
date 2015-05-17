# -*- coding: UTF-8 -*-
__author__ = 'guyh'
from base.httpbase import http
from ctrip.ctripmethod import url,flightschedule
import unittest
from base.trd import china_decode
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


####################################
# CASI003_ST001
# 航班号格式覆盖，返回type为flightschedule
####################################
class Test_flightschedule(unittest.TestCase):
    flightschedule1 = flightschedule.flightschedule1()

    def flightschedule11(self):
        typevlue = self.flightschedule1.type()
        error = 0
        for n in range(len(self.flightschedule1.keyword())):
            keyword = self.flightschedule1.keyword()[n]
            urlvlue = url.url_keyword(china_decode.chinese_decode(str(self.flightschedule1.keyword()[n])))
            tpyevluecompile = http.get_key_vlue(urlvlue,http.vluecount(urlvlue,"word",keyword),"type")
            if tpyevluecompile == typevlue:
                print self.flightschedule1.keyword()[n],"类型正确为",tpyevluecompile
            else :
                error = error+1
                print self.flightschedule1.keyword()[n],"类型错误为",tpyevluecompile
        assert error == 0

