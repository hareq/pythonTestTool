__author__ = 'guyh'
# -*- coding: UTF-8 -*-
__author__ = 'guyh'
import re



def str_find_between(url,a,b):
    print a,b
    c = "(?<="+a+").*?(?="+b+")"
    print c
    return re.findall(c,url,re.DOTALL)

#print str_find_between('abc',"a","c")