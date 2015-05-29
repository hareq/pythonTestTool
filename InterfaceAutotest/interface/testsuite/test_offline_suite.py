
# -*- coding: UTF-8 -*-
__author__ = 'guyh'

import unittest
import HTMLTestRunner
from interface.testcase import Test_offline


def Test_offline_suite():
    filename="Test_offline.html"
    fp=file(filename,'wb')
    testsuite=unittest.TestSuite()
    testsuite.addTest(Test_offline.Test_offline("errcode_Test"))
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='errcode_Test',description='errcode_Test')
    runner.run(testsuite)

    testsuite1=unittest.TestSuite()
    testsuite1.addTest(Test_offline.Test_offline("web_page_hotel"))
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='web_page_hotel',description='web_page_hotel')
    runner.run(testsuite1)