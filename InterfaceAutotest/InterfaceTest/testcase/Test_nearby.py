# -*- coding: UTF-8 -*-
__author__ = 'guyh'
import unittest
import sys

from Framework.httpbase import http


reload(sys)
sys.setdefaultencoding('utf-8')

class Test_nearby(unittest.TestCase):
    def nearby_hotle_price_no_null_Test(self):
        error = 0
        url = ['http://10.8.91.244:8180/appautocomplete/search?keyword=%e9%99%84%e8%bf%91&action=autocomplete&source=globalapp65&lon=121.35801673&lat=31.22016018&districtid=2&type=fortest',
                'http://10.8.91.244:8180/appautocomplete/search?keyword=%e9%99%84%e8%bf%91&action=autocomplete&source=globalapp65&lon=120.545916&lat=31.315913&districtid=100066&type=fortest',
                'http://10.8.91.244:8180/appautocomplete/search?keyword=%e9%99%84%e8%bf%91&action=autocomplete&source=globalapp65&lon=120.984205&lat=31.393074&districtid=77&type=fortest',
                'http://10.8.91.244:8180/appautocomplete/search?keyword=%e9%99%84%e8%bf%91&action=autocomplete&source=globalapp65&lon=114.055626&lat=22.316061&districtid=38&type=fortest',
                'http://10.8.91.244:8180/appautocomplete/search?keyword=%e9%99%84%e8%bf%91&action=autocomplete&source=globalapp65&lon=121.090235&lat=24.17594&districtid=100076&type=fortest',
                'http://10.8.91.244:8180/appautocomplete/search?keyword=%e9%99%84%e8%bf%91&action=autocomplete&source=globalapp65&lon=2.294481&lat=48.85837&districtid=100024&type=fortest',
                'http://10.8.91.244:8180/appautocomplete/search?keyword=%e9%99%84%e8%bf%91&action=autocomplete&source=globalapp65&lon=2.294481&lat=48.85837&districtid=308&type=fortest']
        for n in range(len(url)):
            content = http.getresponse_url_python(url[n])
            for m in range(len(content["data"])):
                try:
                    a = http.get_key_vlue(url[n],m,"price")
                    if a == "null":
                        error = error+1
                        print url[n]
                except Exception:
                    1 == 1
        assert error == 0

