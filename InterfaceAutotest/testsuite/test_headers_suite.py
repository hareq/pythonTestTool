# -*- coding: UTF-8 -*-
__author__ = 'guyh'


import unittest
import HTMLTestRunner
from testcase import Test_headers


def Test_headers_suite():
    filename="D:\work\code\http_interface_autotest\http_interface_autotest\Test_headers.html"
    fp=file(filename,'wb')
    testsuite=unittest.TestSuite()
    testsuite.addTest(Test_headers.Test_headers("headers_ContentType_Test"))
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='Test_headers',description='headers_ContentType_Test')
    runner.run(testsuite)

