# -*- coding: UTF-8 -*-
__author__ = 'guyh'

from appium import webdriver  #导入python版的 appium(webdriver)模块

#定义驱动的参数
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.1.2'
desired_caps['deviceName'] = 'TA00402J3P'
desired_caps['fullReset'] = 'true'
desired_caps['test'] = "D:\work\guappautotest\guapp\Ctrip_V6.6_sit8.1_product_1368339.apk"
desired_caps['appPackage'] = 'ctrip.android.view'
desired_caps['appActivity'] = 'ctrip.android.view.home.CtripSplashActivity'

