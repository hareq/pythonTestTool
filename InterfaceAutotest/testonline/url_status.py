# -*- coding: UTF-8 -*-
__author__ = 'guyh'
import urllib
import sys

from common.ctrip import loadkeyword
from common.trd.httpbase import http
from common.ctrip import logger
import time

log = logger.logger()

keyword_num = 0
word_num = 0
error_url = 0
try:
    for keyword in loadkeyword.load_keyword_from_AppTestCase():
        keyword_num = keyword_num+1
        reload(sys)
        sys.setdefaultencoding('utf-8')
        keyword = str(keyword)
        keyword_quote = urllib.quote(keyword)
        url1 = "http://10.8.119.199:8180/appautocomplete/search?keyword=keywordvalue&action=autocomplete&source=globalonline"
        url1 = url1.replace("keywordvalue",keyword_quote)
        try:
          result1 = http.getresponse_url_python(url1)
        except:
            pass

        for n in result1["data"]:
            time.sleep(1)
            result1 = http.getresponse_url(url1)
            if http.getresponse_status(n["url"]) != 200:
                print http.getresponse_status(n["url"]),keyword,n["word"],n["url"]
except:
    pass
