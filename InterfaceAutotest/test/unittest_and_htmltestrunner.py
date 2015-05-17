# -*- coding: UTF-8 -*-
__author__ = 'guyh'
from selenium import webdriver
import unittest
import time
import HTMLTestRunner
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class DefaultWidgetSizeTestCase(unittest.TestCase):
    def runTest(self):
        i = 0
        for i in range(5):
                print 'a '
        #assert 1 == 1,'测试'+'bb'
    def runTest1(self):
        print 'ccvv'
        self.assertEqual(1,2)


testsuite=unittest.TestSuite()
testsuite.addTest(DefaultWidgetSizeTestCase("runTest"))
testsuite.addTest(DefaultWidgetSizeTestCase("runTest1"))
filename="result.html"
fp=file(filename,'wb')
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='Result1',description='ruTest')
runner.run(testsuite)