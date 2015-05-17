# -*- coding: UTF-8 -*-

__author__ = 'guyh'

import yaml
def dataMap():
    # s = file('a.yaml','w')
    # aa = 'bb'
    # yaml.dump(yaml.load(aa),s)
    f = file('D:\work\code\http_interface_autotest\http_interface_autotest\Framework\data\searchtree.yaml','r')
    #f = open('a.yaml')
    dataMap = yaml.load(f)
    f.close()
    return dataMap
