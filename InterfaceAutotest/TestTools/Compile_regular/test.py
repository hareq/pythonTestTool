# -*- coding: UTF-8 -*-
__author__ = 'guyh'
import yaml
import re

def loadYaml():
    f = file('config/compileconfig.yaml','r')
    rules = yaml.load(f)["config"]
    for n in range(len(rules)):
        if rules[n]["p"]["type"] == "ignore_vlue":
            print "a",n
            print rules[n]["p"]["where"].keys()[0]
            #rules.add(IgnoreRUle)
        else :
            print "b",n

    #return rules;
#loadYaml()

subject = '{"word": "aa","type": "desthotel","price": "188","star": "aa","zonename": "aa 1470.aa","districtname": "aa","url": "ctrip://wireless/InlandHotel?checkInDate=20150518&checkOutDate=20150519&hotelId=436187"},'
subject1 = "aaa"
newstring = ""
regex = "aa"
print regex
number = re.subn(regex, newstring, subject1)
print number
