# -*- coding: UTF-8 -*-
__author__ = 'guyh'

import unittest
import HTMLTestRunner

from app_test.case.testcase import test_channel,test_dest_channel


def test_suite():
    filename = r"App_autu_testl.html"
    fp = file(filename, 'wb')

    testsuite=unittest.TestSuite()
    testsuite.addTest(test_channel.Test_channel("channelplane_test"))
    testsuite.addTest(test_channel.Test_channel("channelhotel_test"))
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test_channel', description='Test_channel')
    runner.run(testsuite)

    testsuite=unittest.TestSuite()
    testsuite.addTest(test_dest_channel.Test_dest_channel("channelplane_test"))
    testsuite.addTest(test_dest_channel.Test_dest_channel("channelhotel_test"))
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test_dest_channel', description='Test_dest_channel')
    runner.run(testsuite)