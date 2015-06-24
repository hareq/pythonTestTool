# -*- coding: UTF-8 -*-

__author__ = 'guyh'
import sys
import urllib

from common.trd.httpbase import http
from compare_ctrip.src.common import filter, loadreg, filewrite_leftpart,filewrite_filterpart
from compare_ctrip.src.common import urlget
from common.ctrip import loadkeyword, logger


log = logger.logger()

def compile_result(testobj):
    log.info("start compile_result")
    try:
        filename_leftpart1 = "output"+"\\"+"leftpart"+"\\"+testobj+"error1.txt"
        filename_leftpart2 = "output"+"\\"+"leftpart"+"\\"+testobj+"error2.txt"

        filename_filterpart1 = "output"+"\\"+"filterpart"+"\\"+testobj+"error1.txt"
        filename_filterpart2 = "output"+"\\"+"filterpart"+"\\"+testobj+"error2.txt"

        f1 = open(filename_leftpart1, 'w')
        f2 = open(filename_leftpart2, 'w')

        f3 = open(filename_filterpart1, 'w')
        f4 = open(filename_filterpart2, 'w')

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
            result3 = result1
            result4 = result2
            result5 = result1
            result6 = result2


            for m in loadreg.loadreg():
                result5 = filter.leftpart(result5, m)
                result6 = filter.leftpart(result6, m)
                result3 = filter.ignorepart(result5, m)
                result4 = filter.ignorepart(result5, m)



            if result5 == result6:
                log.info(keyword)
                log.info(testobj)
                log.info("完全一致")
            else:
                log.info(keyword)
                log.info(testobj)
                log.info("存在不同")

            #time.sleep(1)
            filewrite_filterpart.filewrite_filterpart(f3,result3,keyword)
            filewrite_filterpart.filewrite_filterpart(f4,result4,keyword)
            filewrite_leftpart.filewrite_leftpart(f1,result5,keyword)
            filewrite_leftpart.filewrite_leftpart(f2,result6,keyword)



    except Exception,e:
        log.error(e)
