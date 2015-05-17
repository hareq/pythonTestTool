# -*- coding: UTF-8 -*-
__author__ = 'guyh'
from base.httpbase import http
from ctrip.ctripmethod import url,channel
import unittest
from base.trd import china_decode
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class Test_channel(unittest.TestCase):
    channelplane = channel.channelplane()
    channelhotel = channel.channelhotel()
    channelticket = channel.channelticket()
    feature = channel.feature()
    channeltravel = channel.channeltravel()
    travelgroup = channel.travelgroup()
    flighthotel = channel.flighthotel()
    channelgroup = channel.channelgroup()
    channeltrain = channel.channeltrain()
    channelbus = channel.channelbus()
    channelgs = channel.channelgs()
    channeltrain = channel.channeltrain()


    def channelplane_Test(self):
        typevlue = self.channelplane.type()
        error = 0
        for n in range(len(self.channelplane.keyword())):
            keyword = self.channelplane.keyword()[n]
            urlvlue = url.url_keyword(china_decode.chinese_decode(str(self.channelplane.keyword()[n])))
            tpyevluecompile = http.get_key_vlue(urlvlue,http.vluecount(urlvlue,"word",keyword),"type")
            if tpyevluecompile == typevlue:
                print self.channelplane.keyword()[n],"类型正确为",tpyevluecompile
            else :
                error = error+1
                print self.channelplane.keyword()[n],"类型错误为",tpyevluecompile
        assert error == 0


    def channelhotel_Test(self):
        typevlue = self.channelhotel.type()
        error = 0
        for n in range(len(self.channelhotel.keyword())):
            keyword = self.channelhotel.keyword()[n]
            urlvlue = url.url_keyword(china_decode.chinese_decode(str(self.channelhotel.keyword()[n])))
            tpyevluecompile = http.get_key_vlue(urlvlue,http.vluecount(urlvlue,"word",keyword),"type")
            if tpyevluecompile == typevlue:
                print self.channelhotel.keyword()[n],"类型正确为",tpyevluecompile
            else :
                error = error+1
                print self.channelhotel.keyword()[n],"类型错误为",tpyevluecompile
        assert error == 0

    def channelticket_Test(self):
        typevlue = self.channelticket.type()
        error = 0
        for n in range(len(self.channelticket.keyword())):
            keyword = self.channelticket.keyword()[n]
            urlvlue = url.url_keyword(china_decode.chinese_decode(str(self.channelticket.keyword()[n])))
            tpyevluecompile = http.get_key_vlue(urlvlue,http.vluecount(urlvlue,"word",keyword),"type")
            if tpyevluecompile == typevlue:
                print self.channelticket.keyword()[n],"类型正确为",tpyevluecompile
            else :
                error = error+1
                print self.channelticket.keyword()[n],"类型错误为",tpyevluecompile
        assert error == 0

    def feature_Test(self):
        typevlue = self.feature.type()
        error = 0
        for n in range(len(self.feature.keyword())):
            keyword = self.feature.keyword()[n]
            urlvlue = url.url_keyword(china_decode.chinese_decode(str(self.feature.keyword()[n])))
            tpyevluecompile = http.get_key_vlue(urlvlue,http.vluecount(urlvlue,"word",keyword),"type")
            if tpyevluecompile == typevlue:
                print self.feature.keyword()[n],"类型正确为",tpyevluecompile
            else :
                error = error+1
                print self.feature.keyword()[n],"类型错误为",tpyevluecompile
        assert error == 0

    def channeltravel_Test(self):
        typevlue = self.channeltravel.type()
        error = 0
        for n in range(len(self.channeltravel.keyword())):
            keyword = self.channeltravel.keyword()[n]
            urlvlue = url.url_keyword(china_decode.chinese_decode(str(self.channeltravel.keyword()[n])))
            tpyevluecompile = http.get_key_vlue(urlvlue,http.vluecount(urlvlue,"word",keyword),"type")
            if tpyevluecompile == typevlue:
                print self.channeltravel.keyword()[n],"类型正确为",tpyevluecompile
            else :
                error = error+1
                print self.channeltravel.keyword()[n],"类型错误为",tpyevluecompile
        assert error == 0

    def travelgroup_Test(self):
        typevlue = self.travelgroup.type()
        error = 0
        for n in range(len(self.travelgroup.keyword())):
            keyword = self.travelgroup.keyword()[n]
            urlvlue = url.url_keyword(china_decode.chinese_decode(str(self.travelgroup.keyword()[n])))
            tpyevluecompile = http.get_key_vlue(urlvlue,http.vluecount(urlvlue,"word",keyword),"type")
            if tpyevluecompile == typevlue:
                print self.travelgroup.keyword()[n],"类型正确为",tpyevluecompile
            else :
                error = error+1
                print self.travelgroup.keyword()[n],"类型错误为",tpyevluecompile
        assert error == 0

    def flighthotel_Test(self):
        typevlue = self.flighthotel.type()
        error = 0
        for n in range(len(self.flighthotel.keyword())):
            keyword = self.flighthotel.keyword()[n]
            urlvlue = url.url_keyword(china_decode.chinese_decode(str(self.flighthotel.keyword()[n])))
            tpyevluecompile = http.get_key_vlue(urlvlue,http.vluecount(urlvlue,"word",keyword),"type")
            if tpyevluecompile == typevlue:
                print self.flighthotel.keyword()[n],"类型正确为",tpyevluecompile
            else :
                error = error+1
                print self.flighthotel.keyword()[n],"类型错误为",tpyevluecompile
        assert error == 0

    def channelgroup_Test(self):
        typevlue = self.channelgroup.type()
        error = 0
        for n in range(len(self.channelgroup.keyword())):
            keyword = self.channelgroup.keyword()[n]
            urlvlue = url.url_keyword(china_decode.chinese_decode(str(self.channelgroup.keyword()[n])))
            tpyevluecompile = http.get_key_vlue(urlvlue,http.vluecount(urlvlue,"word",keyword),"type")
            if tpyevluecompile == typevlue:
                print self.channelgroup.keyword()[n],"类型正确为",tpyevluecompile
            else :
                error = error+1
                print self.channelgroup.keyword()[n],"类型错误为",tpyevluecompile
        assert error == 0

    def channeltrain_Test(self):
        typevlue = self.channeltrain.type()
        error = 0
        for n in range(len(self.channeltrain.keyword())):
            keyword = self.channeltrain.keyword()[n]
            urlvlue = url.url_keyword(china_decode.chinese_decode(str(self.channeltrain.keyword()[n])))
            tpyevluecompile = http.get_key_vlue(urlvlue,http.vluecount(urlvlue,"word",keyword),"type")
            if tpyevluecompile == typevlue:
                print self.channeltrain.keyword()[n],"类型正确为",tpyevluecompile
            else :
                error = error+1
                print self.channeltrain.keyword()[n],"类型错误为",tpyevluecompile
        assert error == 0

    def channelbus_Test(self):
        typevlue = self.channelbus.type()
        error = 0
        for n in range(len(self.channelbus.keyword())):
            keyword = self.channelbus.keyword()[n]
            urlvlue = url.url_keyword(china_decode.chinese_decode(str(self.channelbus.keyword()[n])))
            tpyevluecompile = http.get_key_vlue(urlvlue,http.vluecount(urlvlue,"word",keyword),"type")
            if tpyevluecompile == typevlue:
                print self.channelbus.keyword()[n],"类型正确为",tpyevluecompile
            else :
                error = error+1
                print self.channelbus.keyword()[n],"类型错误为",tpyevluecompile
        assert error == 0

    def channelgs_Test(self):
        typevlue = self.channelgs.type()
        error = 0
        for n in range(len(self.channelgs.keyword())):
            keyword = self.channelgs.keyword()[n]
            urlvlue = url.url_keyword(china_decode.chinese_decode(str(self.channelgs.keyword()[n])))
            tpyevluecompile = http.get_key_vlue(urlvlue,http.vluecount(urlvlue,"word",keyword),"type")
            if tpyevluecompile == typevlue:
                print self.channelgs.keyword()[n],"类型正确为",tpyevluecompile
            else :
                error = error+1
                print self.channelgs.keyword()[n],"类型错误为",tpyevluecompile
        assert error == 0


    def channeltrain_Test(self):
        typevlue = self.channeltrain.type()
        error = 0
        for n in range(len(self.channeltrain.keyword())):
            keyword = self.channeltrain.keyword()[n]
            urlvlue = url.url_keyword(china_decode.chinese_decode(str(self.channeltrain.keyword()[n])))
            tpyevluecompile = http.get_key_vlue(urlvlue,http.vluecount(urlvlue,"word",keyword),"type")
            if tpyevluecompile == typevlue:
                print self.channeltrain.keyword()[n],"类型正确为",tpyevluecompile
            else :
                error = error+1
                print self.channeltrain.keyword()[n],"类型错误为",tpyevluecompile
        assert error == 0







