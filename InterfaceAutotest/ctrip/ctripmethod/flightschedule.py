# -*- coding: UTF-8 -*-
__author__ = 'guyh'
from base.trd import yamltool


class flightschedule1:
     def keyword(self):
         return yamltool.dataMap()["flightschedule"]["flightschedule1"]["keyword"].split(",")

     def type(self):
         return yamltool.dataMap()["flightschedule"]["flightschedule1"]["type"]

class flightschedule2:
     def keyword(self):
         return yamltool.dataMap()["flightschedule"]["flightschedule2"]["keyword"].split(",")
     def type(self):
         return yamltool.dataMap()["flightschedule"]["flightschedule2"]["type"]

class flightschedule3:
     def keyword(self):
         return yamltool.dataMap()["flightschedule"]["flightschedule3"]["keyword"].split(",")

     def type(self):
         return yamltool.dataMap()["flightschedule"]["flightschedule3"]["type"]

#channelkeywordall()