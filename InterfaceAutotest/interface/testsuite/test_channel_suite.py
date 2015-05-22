# -*- coding: UTF-8 -*-
__author__ = 'guyh'

import unittest
import HTMLTestRunner

from TestInterface.testcase import Test_channel


def Test_channel_suite():
    filename="D:\work\code\http_interface_autotest\http_interface_autotest\Test_channel.html"
    fp=file(filename,'wb')

    testsuite=unittest.TestSuite()
    testsuite.addTest(Test_channel.Test_channel("channelplane_Test"))
    testsuite.addTest(Test_channel.Test_channel("channelhotel_Test"))
    testsuite.addTest(Test_channel.Test_channel("channelticket_Test"))
    testsuite.addTest(Test_channel.Test_channel("feature_Test"))
    testsuite.addTest(Test_channel.Test_channel("channeltravel_Test"))
    testsuite.addTest(Test_channel.Test_channel("travelgroup_Test"))
    testsuite.addTest(Test_channel.Test_channel("flighthotel_Test"))
    testsuite.addTest(Test_channel.Test_channel("channelgroup_Test"))
    testsuite.addTest(Test_channel.Test_channel("channelbus_Test"))
    testsuite.addTest(Test_channel.Test_channel("channelgs_Test"))
    testsuite.addTest(Test_channel.Test_channel("channeltrain_Test"))
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='Test_channel',description='频道词测试')
    runner.run(testsuite)

