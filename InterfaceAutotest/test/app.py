# -*- coding: UTF-8 -*-
__author__ = 'guyh'

from appium import webdriver  #导入python版的 appium(webdriver)模块

#定义驱动的参数
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = 'C2J6R14C09000822'
desired_caps['fullReset'] = 'true'
desired_caps['app'] = "D:\work\guappautotest\guapp\Ctrip_Wireless_View_V6.4.1_SIT2_PRODUCT.apk"
#desired_caps['appPackage'] = 'ctrip.android.view'
#desired_caps['appActivity'] = 'ctrip.android.view.home.CtripSplashActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
el = driver.find_element_by_name("目的地/酒店/景点/航班号")
el.click()

textfields = driver.find_elements_by_tag_name("textfield")
textfields[0].send_keys("My Name")
textfields[2].send_keys("someone@somewhere.com")

driver.find_element_by_name("Save").click()

driver.quit()
