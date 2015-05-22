# -*- coding: UTF-8 -*-
__author__ = 'guyh'

import unittest
import HTMLTestRunner

from interface.testcase import Test_nearby


def Test_nearby_suite():
    filename="D:\work\code\http_interface_autotest\http_interface_autotest\Test_nearby.html"
    fp=file(filename,'wb')
    testsuite=unittest.TestSuite()
    testsuite.addTest(Test_nearby.Test_nearby("nearby_hotle_price_no_null_Test"))
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='Test_nearby',description='nearby_hotle_price_no_null_Test')
    runner.run(testsuite)

