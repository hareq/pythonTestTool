# -*- coding: UTF-8 -*-
__author__ = 'guyh'
from selenium import webdriver
import unittest
import unittest
import HTMLTestRunner
from interface.testcase import Test_offline
import json

def check_point_title(jsonstr,browser):
    #jsonstr = json.loads(jsonstr)
    browser.get(jsonstr["url"])
    print jsonstr["url"]
    if jsonstr["word"] in browser.title:
        a = 1
    else:
        a = 0
    return a,jsonstr["word"],browser.title




