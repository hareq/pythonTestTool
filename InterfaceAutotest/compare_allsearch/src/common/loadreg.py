# -*- coding: UTF-8 -*-
__author__ = 'guyh'

import sys

def loadreg():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    f = open('config\cfg_allsearch\ignorereg', 'r')
    return f.read().split("\n")