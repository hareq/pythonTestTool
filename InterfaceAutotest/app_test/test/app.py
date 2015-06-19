# -*- coding: UTF-8 -*-
__author__ = 'guyh'

from appium import webdriver  #导入python版的 appium(webdriver)模块
from app_test.resource import drivesconfig
#定义驱动的参数

desired_caps = drivesconfig.desired_caps

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.find_element_by_name("目的地/酒店/景点/航班号").click()
textfields = driver.find_elements_by_tag_name("textfield")
textfields[0].send_keys("My Name")
textfields[2].send_keys("someone@somewhere.com")

driver.find_element_by_name("Save").click()

driver.quit()
