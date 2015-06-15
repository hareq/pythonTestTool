# -*- coding: UTF-8 -*-
__author__ = 'guyh'
import sys
import urllib

from common.ctrip import loadkeyword
from common.trd.httpbase import http
from common.trd.httpbase import http


m = []

for keyword in loadkeyword.load_keyword_from_AppTestCase():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    keyword = str(keyword)
    keyword_quote = urllib.quote(keyword)
    url = "http://10.2.25.24:8180/appautocomplete/search?keyword=keywordvalue&action=autocomplete&source=globalonline"
    url1 = url.replace("keywordvalue",keyword_quote)
    result1 = http.getresponse_url(url1)
    try:
        result1 = http.json_to_py(result1)
        for n in result1["data"]:
            if "m.ctrip.com" in n["url"]:
                print keyword,n["word"],n["type"],n["url"]
                if n["type"] not in m:
                    m.append(n["type"])
                    #print keyword,n["word"],n["type"],n["url"]
    except Exception:
        pass
print m
