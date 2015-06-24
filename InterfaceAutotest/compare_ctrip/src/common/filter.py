# -*- coding: UTF-8 -*-
__author__ = 'ming.zhang'

import re
import sys

def splitSrc(src):
    pattern = re.compile("\{.*?\}",re.S)
    return pattern.finditer(src)

def prepareString(src):
    #temp = unicode(src.strip(),  "UTF-8")
    temp = src.strip()
    if (temp[0] == '{'):
        temp= temp[1:]
    return temp;

def getPairPattern(regStr):
    temp = regStr.replace("(","SPECIALMARK")
    temp = temp.replace(")","(")
    temp = temp.replace("SPECIALMARK",")")
    temp = "("+temp+")"
    temp = temp.replace("()","")
    return re.compile(temp,re.S)

def filter(src,regStr):
    pattern = re.compile(regStr,re.S)
    pairPattern = getPairPattern(regStr)
    stringLeft=prepareString(src)
    result=[]
    for subSrc in splitSrc(prepareString(src)):
        #print subSrc.group(0)
        matchIterator = pattern.finditer(subSrc.group(0))
        flag = False
        for match in matchIterator:
            fullString = match.group(0)
            temp = pairPattern.match(fullString)
            if (temp):
                # for  group in temp.groups():
                # #	print group
                    # replaceString = replaceString+group
                replaceString=unicode("",  "UTF-8").join(temp.groups())
                #print fullString
                #print replaceString
                stringLeft=stringLeft.replace(fullString,replaceString)
                #print match.groups()
                result.append(match.groups())
                flag=True
    result.append(stringLeft)
    return result

def leftpart(src,regStr):
    return "{"+filter(src,regStr)[len(filter(src,regStr))-1]

def ignorepart(src,regStr):
    if len(filter(src,regStr))>2:
        for n in (len(filter(src,regStr))-1):
            pass




#print len(filter(str1,regular_config))
#print filter(str1,regular_config)[59]

