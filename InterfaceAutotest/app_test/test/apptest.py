# -*- coding: UTF-8 -*-
__author__ = 'guyh'

from appium import webdriver  #导入python版的 appium(webdriver)模块

#定义驱动的参数
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
#在命令行中输入“adb shell”"adb devices"或者启动hierachyviewer查看
desired_caps['deviceName'] = 'TA00402J3P'
#adb logcat -c
#adb logcat ActivityManager:I *:s
desired_caps['appPackage'] = 'com.android.chrome'
desired_caps['appActivity'] = 'com.google.android.apps.chrome.ChromeTabbedActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.find_element_by_id("com.android.chrome:id/url_bar").click()