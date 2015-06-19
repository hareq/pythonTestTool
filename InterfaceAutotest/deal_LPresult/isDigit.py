# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 18:24:00 2014

@author: yi_liu
"""

def check_isDigit(filed_str):
    strList=filed_str.split('.')
    if len(strList) == 1:
        if strList[0].isdigit():
            return 1
        else:
            print "%s is not a  numeric."%filed_str
            return 0
    elif len(strList) == 2:
        if strList[0].isdigit() and strList[1].isdigit() :
            return 1
        else:
            print "%s is not a  numeric."%filed_str
            return 0
    else:
        print "%s is not a  numeric."%filed_str
        return 0
        
#filed_str='.67'
#print "filed_str",filed_str
#print "return :",check_isDigit(filed_str)
    