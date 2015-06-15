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

for keyword in loadkeyword.load_keyword_from_AppTestCase():
    time.sleep(1)
    keyword_num = keyword_num+1
    reload(sys)
    sys.setdefaultencoding('utf-8')
    keyword = str(keyword)
    keyword_quote = urllib.quote(keyword)
    url1 = "http://10.8.91.244:8180/appautocomplete/search?keyword=keywordvalue&action=autocomplete&source=globalonline&type=test"
    url1 = url1.replace("keywordvalue",keyword_quote)
    url2 = "http://10.8.91.244:8140/qrwservice/search?source=globalonline&action=autocomplete&keyword=keywordvalue&type=test"
    url2 = url2.replace("keywordvalue",keyword_quote)
    result1 = http.getresponse_url(url1)
    result2 = http.getresponse_url(url2)
    try:
        result1 = http.json_to_py(result1)
        result2 = http.json_to_py(result2)
        for n in result1["data"]:
            word_num = word_num+1
            for m in result2["data"]:
                time.sleep(1)
                if n["word"] == m["word"]:
                    if n["url"] == m["url"]:
                        log.info(keyword),log.info(n["word"]),log.info("url相同")

                    else:
                        # if "m.ctrip.com" in n["url"]:#新的url存在m.ctrip.com
                        #     pass
                        # elif ".html" not in n["url"] and ".html" in m["url"]:#新的url没有.html，跳转为404
                        #     pass
                        if "international" in n["url"] and "hotel" in m["url"]:
                            pass
                        elif "TrainBooking" in n["url"]:
                            pass
                        elif "huodong" in n["url"] and "you.ctrip.com" in m["url"]:
                            pass
                        elif "food" in n["url"]:
                            pass
                        elif "keyword" in n["url"] or "keyword" in m["url"]:#新的url的keyword传值错误
                            pass
                        elif "place" in n["url"] and "lvyou" in m["url"]:#目的地新的为攻略目的地主页，旧的为攻略目的地游玩
                            pass
                        elif str(n["url"]).lower() == str(m["url"]).lower():#新旧存在大小写不同
                            pass
                        else:
                            error_url = error_url+1
                            #log.info(keyword),log.info(n["word"]),log.info("url不相同")
                            print keyword,n["word"],"url不相同"
                            print "new",n["url"]
                            print "old",m["url"]
                    #print keyword,n["word"],n["type"],n["url"]
    except Exception:
        pass
print "一共测试了：",keyword_num,"个关键字"
print "一共测试了：",word_num,"个联想词"
print "一共出现不一致的url共：",error_url,"个"

