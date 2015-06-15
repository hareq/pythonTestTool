# -*- coding: utf-8 -*-
__author__ = 'guyh'

import urllib
from array import array
def chinese_decode(vlue):
    return urllib.quote(vlue)


print chinese_decode("上海")
a = u'\xb3\xc2\xbd\xa8\xc3\xf4'
b = array('u', a).tostring()[::2].decode('gbk')


print b
#print a.decode('gb18030').encode('utf-8')