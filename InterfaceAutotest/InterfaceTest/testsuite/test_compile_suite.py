# -*- coding: UTF-8 -*-
__author__ = 'guyh'

import unittest
import HTMLTestRunner

from TestInterface.testcase import Test_compile_flyback


def Test_compile_suite():

    filename="D:\work\code\http_interface_autotest\http_interface_autotest\Test_compile.html"
    fp1=file(filename,'wb')

    testsuite_Test_compile=unittest.TestSuite()
    testsuite_Test_compile.addTest(Test_compile_flyback.Test_compile("ipcompileTest"))
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp1,title='Test_compile',description='不同Get访问结果对比测试')
    runner.run(testsuite_Test_compile)

