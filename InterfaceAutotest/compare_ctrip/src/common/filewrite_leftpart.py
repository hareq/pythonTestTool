# -*- coding: UTF-8 -*-
__author__ = 'guyh'
import sys

def filewrite_leftpart(f,val1,val2):

    reload(sys)
    sys.setdefaultencoding('utf-8')
    f.write("############################################")
    f.write("\n")
    f.write(val2)
    f.write("\n")
    f.write("############################################")
    f.write("\n")
    f.write(val1.replace(",","\n"))
    f.write("\n")