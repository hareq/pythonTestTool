#-*- coding:utf-8 -*-

import  xml.dom.minidom


def getnodeValue(text,TagName,Attribute):
    dom = xml.dom.minidom.parse(text)
    root = dom.documentElement
    itemlist = root.getElementsByTagName(TagName)
    item = itemlist[0]
    un = item.getAttribute(Attribute)
    return un
     
