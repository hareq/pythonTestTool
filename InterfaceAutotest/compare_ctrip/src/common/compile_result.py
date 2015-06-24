# -*- coding: UTF-8 -*-

__author__ = 'guyh'
import sys
import urllib

from common.trd.httpbase import http
from compare_ctrip.src.common import filter, loadreg, filewrite
from compare_ctrip.src.common import urlget
from common.ctrip import loadkeyword, logger


log = logger.logger()

def compile_result(testobj):
    log.info("start compile_result")
    try:
        filename1 = "output"+"\\"+testobj+"error1.txt"
        filename2 = "output"+"\\"+testobj+"error2.txt"
        f1 = open(filename1, 'w')
        f2 = open(filename2, 'w')
        log.info("start get keyword")
        for keyword in loadkeyword.load_keyword_from_AppTestCase():
            reload(sys)
            sys.setdefaultencoding('utf-8')
            keyword = str(keyword)
            keyword_quote = urllib.quote(keyword)
            url1 = urlget.urlall(urlget.urlget(testobj)["url1"],keyword_quote)
            url2 = urlget.urlall(urlget.urlget(testobj)["url2"],keyword_quote)

            log.info("start http getresponse_url")

            result1 = http.getresponse_url(url1)
            result2 = http.getresponse_url(url2)

            for m in loadreg.loadreg():
                result1 = filter.leftpart(result1, m)
                result2 = filter.leftpart(result2, m)

            if result1 == result2:
                log.info(keyword)
                log.info(testobj)
                log.info("完全一致")
            else:
                log.info(keyword)
                log.info(testobj)
                log.info("存在不同")

            #time.sleep(1)
            filewrite.filewrite(f1,result1,keyword)
            filewrite.filewrite(f2,result2,keyword)
    except Exception,e:
        log.error(e)
