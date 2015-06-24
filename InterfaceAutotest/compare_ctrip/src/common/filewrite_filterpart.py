# -*- coding: UTF-8 -*-
__author__ = 'guyh'
import sys

def filewrite_filterpart(f,val1,val2):
    if val1 != []:
        for n in val1:
            reload(sys)
            sys.setdefaultencoding('utf-8')
            f.write("############################################")
            f.write("\n")
            f.write(val2)
            f.write("\n")
            f.write("############################################")
            f.write("\n")
            f.write(val1.n(",","\n"))
            f.write("\n")
    else:
        pass