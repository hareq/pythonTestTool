# -*- coding: UTF-8 -*-
__author__ = 'guyh'
from base.trd import yamltool


class channelplane:
     def keyword(self):
         return yamltool.dataMap()["channel"]["channelplane"]["keyword"].split(",")

     def same(self):
         return yamltool.dataMap()["channel"]["channelplane"]["same"].split(",")

     def type(self):
         return yamltool.dataMap()["channel"]["channelplane"]["type"]


class channelhotel:
     def keyword(self):
         return yamltool.dataMap()["channel"]["channelhotel"]["keyword"].split(",")

     def type(self):
         return yamltool.dataMap()["channel"]["channelhotel"]["type"]

class channelticket:
     def keyword(self):
         return yamltool.dataMap()["channel"]["channelticket"]["keyword"].split(",")

     def type(self):
         return yamltool.dataMap()["channel"]["channelticket"]["type"]

class channelgs:
     def keyword(self):
         return yamltool.dataMap()["channel"]["channelgs"]["keyword"].split(",")

     def type(self):
         return yamltool.dataMap()["channel"]["channelgs"]["type"]

class channeltravel:
     def keyword(self):
         return yamltool.dataMap()["channel"]["channeltravel"]["keyword"].split(",")

     def type(self):
         return yamltool.dataMap()["channel"]["channeltravel"]["type"]

class travelgroup:
     def keyword(self):
         return yamltool.dataMap()["channel"]["travelgroup"]["keyword"].split(",")

     def type(self):
         return yamltool.dataMap()["channel"]["travelgroup"]["type"]

class flighthotel:
     def keyword(self):
         return yamltool.dataMap()["channel"]["flighthotel"]["keyword"].split(",")

     def type(self):
         return yamltool.dataMap()["channel"]["flighthotel"]["type"]

class channelgroup:
     def keyword(self):
         return yamltool.dataMap()["channel"]["channelgroup"]["keyword"].split(",")

     def type(self):
         return yamltool.dataMap()["channel"]["channelgroup"]["type"]

class channeltrain:
     def keyword(self):
         return yamltool.dataMap()["channel"]["channeltrain"]["keyword"].split(",")

     def type(self):
         return yamltool.dataMap()["channel"]["channeltrain"]["type"]

class channelbus:
     def keyword(self):
         return yamltool.dataMap()["channel"]["channelbus"]["keyword"].split(",")

     def type(self):
         return yamltool.dataMap()["channel"]["channelbus"]["type"]

class feature:
     def keyword(self):
         return yamltool.dataMap()["channel"]["feature"]["keyword"].split(",")

     def type(self):
         return yamltool.dataMap()["channel"]["feature"]["type"]

class channeltrain:
     def keyword(self):
         return yamltool.dataMap()["channel"]["channeltrain"]["keyword"].split(",")

     def type(self):
         return yamltool.dataMap()["channel"]["channeltrain"]["type"]

def channelkeywordall():
    list = []
    for n in range(len(yamltool.dataMap()["channel"])):
        for m in range(len(yamltool.dataMap()["channel"].items()[n][1]["keyword"].split(","))):
            list.append(yamltool.dataMap()["channel"].items()[n][1]["keyword"].split(",")[m])
    return list

#channelkeywordall()