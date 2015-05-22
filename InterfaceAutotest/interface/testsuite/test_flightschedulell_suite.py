# -*- coding: UTF-8 -*-
__author__ = 'guyh'

import unittest
import HTMLTestRunner

from TestInterface.testcase import Test_flightschedule


def Test_channel_suite():
    filename="D:\work\code\http_interface_autotest\http_interface_autotest\Test_flightschedule1.html"
    fp=file(filename,'wb')

    testsuite=unittest.TestSuite()
    testsuite.addTest(Test_flightschedule.Test_flightschedule("flightschedule11"))

    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='flightschedule1_test',description='航班号测试')
    runner.run(testsuite)

