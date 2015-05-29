# -*- coding: UTF-8 -*-
__author__ = 'guyh'
import unittest
import sys,urllib
from common.httpbase import http
from common.trd import read_excel
from interface.src import loadkeyword
reload(sys)
sys.setdefaultencoding('utf-8')
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from compare_allsearch.src.common import logger

log = logger.logger()

class Test_offline(unittest.TestCase):
    def errcode_Test(self):
        error = 0
        url = "http://10.2.25.24:8180/appautocomplete/search?source=offline&action=autocomplete&keyword=keyword_value"
        for keyword in loadkeyword.load_keyword_from_AppTestCase():
            keyword = str(keyword)
            keyword_quote = urllib.quote(keyword)
            url = url.replace("keyword_value",keyword_quote)
            if http.getresponse_url_python(url)["head"]["errcode"] != 0:
                print keyword,http.getresponse_url_python(url)["head"]["errcode"]
            assert http.getresponse_url_python(url)["head"]["errcode"] == 0


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


    def web_page_marklandhotellist(self):
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
                        if a == "marklandhotellist":
                            b = content["data"][m]["url"]
                            c = content["data"][m]["word"]
                            browser.get(b) # Load page
                            time.sleep(5)
                            if c[:-3] in browser.title:
                                infovalue = "marklandhotellist测试，"+"测试过的关键字为"+keyword+"结果正确"
                                log.info(infovalue)
                            else:
                                error = error+1
                                infovalue = "marklandhotellist测试，"+"测试过的关键字为："+keyword+"结果错误，"+"word="+c[:-3]+"网页title="+browser.title
                                log.info(infovalue)
                                print "marklandhotellist测试错误",keyword,c,c[:-3],browser.title
        except Exception,e:
            log.error(e)

        assert 0 == 0
        browser.close()

    def web_page_districthotellist(self):
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
                        if a == "districthotellist":
                            b = content["data"][m]["url"]
                            c = content["data"][m]["word"]
                            d = content["data"][m]["districtname"]
                            browser.get(b) # Load page
                            time.sleep(5)
                            if d+"酒店" in browser.title:
                                infovalue = "districthotellist测试，"+"测试过的关键字为"+keyword+"结果正确"
                                log.info(infovalue)
                            else:
                                error = error+1
                                infovalue = "districthotellist测试，"+"测试过的关键字为："+keyword+"结果错误，"+"word="+c[:-3]+"网页title="+browser.title
                                log.info(infovalue)
                                print "districthotellist测试错误",keyword,c,d,browser.title
        except Exception,e:
            log.error(e)

        assert 0 == 0
        browser.close()