# -*- coding: UTF-8 -*-
__author__ = 'guyh'

from appium import webdriver  #导入python版的 appium(webdriver)模块

#定义驱动的参数
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = 'C2J6R14C09000822'
#desired_caps['app'] = "D:\work\ppautotest\pp\Ctrip_Wireless_View_V6.4.1_SIT2_PRODUCT.apk"
desired_caps['appPackage'] = 'com.example.android.notepad'
desired_caps['appActivity'] = '.NotesList'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

# el = driver.find_element_by_accessibility_id("New note")
# el.click()
#
# el = driver.find_element_by_class_name("android.widget.EditText")
# el.send_keys("This is a new note!")
#
# el = driver.find_element_by_accessibility_id("Save")
# el.click()
#
# els = driver.find_elements_by_class_name("android.widget.TextView")
#
#
# els[2].click()