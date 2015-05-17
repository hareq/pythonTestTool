# -*- coding: UTF-8 -*-
__author__ = 'guyh'
from base.httpbase import http
from ctrip.ctripmethod import url,channel
import unittest
from base.trd import china_decode
from base.httpmethod import result_compare
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class Test_compile(unittest.TestCase):
    channelplane = channel.channelplane()
    def ipcompileTest(self):

        #channel.channelkeywordall()
        error = 0
        for n in range(len(channel.channelkeywordall())):
            urlvluecompile = url.url_keyword(china_decode.chinese_decode(str(channel.channelkeywordall()[n])))
            urlvlue = url.url_keyword(china_decode.chinese_decode(str(keyword)))
            if result_compare.compare_result_all(urlvlue,urlvluecompile) == 1:
                print channel.channelkeywordall()[n],"对比结果一致，成功"
            if result_compare.compare_result_all(urlvlue,urlvluecompile) == 0:
                error = error+1
                print channel.channelkeywordall()[n],"对比结果不一致，失败"
        assert error == 0