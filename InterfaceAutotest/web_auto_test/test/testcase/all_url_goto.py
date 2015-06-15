__author__ = 'guyh'
# -*- coding: UTF-8 -*-
__author__ = 'guyh'
import sys
import urllib

from common.trd.httpbase import http
from interface.src import loadkeyword

reload(sys)
sys.setdefaultencoding('utf-8')
from selenium import webdriver
import time
from common.ctrip import logger

log = logger.logger()

def web_page_hotel(self):
    try:
        error = 0
        url = "http://10.2.25.24:8180/appautocomplete/search?source=offline&action=autocomplete&keyword=keyword_value"
        browser = webdriver.Firefox()
        for keyword in loadkeyword.load_keyword_from_AppTestCase():
            keyword = str(keyword)
            keyword_quote = urllib.quote(keyword)
            urlnew = url.replace("keyword_value",keyword_quote)
            content = http.getresponse_url_python(urlnew)
            for m in range(len(content["data"])):
                    a = http.get_key_vlue(urlnew,m,"type")
                    if a == "hotel":
                        b = content["data"][m]["url"]
                        c = content["data"][m]["word"]
                        browser.get(b) # Load page
                        time.sleep(5)
                        if c in browser.title:
                            infovalue = "hotel测试，"+"测试过的关键字为"+keyword+"结果正确"
                            log.info(infovalue)
                        else:
                            error = error+1
                            infovalue = "hotel测试，"+"测试过的关键字为："+keyword+"结果错误，"+"word="+c+"网页title="+browser.title
                            log.info(infovalue)
                            print "hotel错误",keyword,c,browser.title
    except Exception,e:
        log.error(e)

    assert error == 0
    browser.close()

