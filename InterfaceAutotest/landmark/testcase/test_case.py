# -*- coding: UTF-8 -*-
__author__ = 'guyh'

from landmark.common_landmark import getdata,geturl,checkpoint



def hotel_test():
    error = 0
    for data in getdata.hotel():
        checkpoint.checkout_base(data)
        checkpoint.checkout_city(data)
        checkpoint.checkout_district(data)
        checkpoint.checkout_downtown(data)
        checkpoint.checkout_province(data)

def markland_test():
    error = 0
    for data in getdata.markland():
        checkpoint.checkout_base(data)
        checkpoint.checkout_city(data)
        checkpoint.checkout_district(data)
        checkpoint.checkout_downtown(data)
        checkpoint.checkout_province(data)

def metrostation_test():
    error = 0
    for data in getdata.metrostation():
        checkpoint.checkout_base(data)
        checkpoint.checkout_city(data)
        checkpoint.checkout_district(data)
        checkpoint.checkout_downtown(data)
        checkpoint.checkout_province(data)

def airport_test():
    error = 0
    for data in getdata.airport():
        checkpoint.checkout_base(data)
        checkpoint.checkout_city(data)
        checkpoint.checkout_district(data)
        checkpoint.checkout_downtown(data)
        checkpoint.checkout_province(data)

def railwaystation_test():
    error = 0
    for data in getdata.railwaystation():
        checkpoint.checkout_base(data)
        checkpoint.checkout_city(data)
        checkpoint.checkout_district(data)
        checkpoint.checkout_downtown(data)
        checkpoint.checkout_province(data)

##下面是按照关键字的类型分类测试
def base_test():
    print "开始关键字测试"
    print "开始hotel_test"
    for data in getdata.hotel():
        checkpoint.checkout_base(data)
    print "开始markland_test"
    for data in getdata.markland():
        checkpoint.checkout_base(data)
    print "开始metrostation_test"
    for data in getdata.metrostation():
        checkpoint.checkout_base(data)
    print "开始airport_test"
    for data in getdata.airport():
        checkpoint.checkout_base(data)
    print "开始railwaystation_test"
    for data in getdata.railwaystation():
        checkpoint.checkout_base(data)

def city_test():
    print "开始关键字测试+城市"
    print "开始hotel_test"
    for data in getdata.hotel():
        checkpoint.checkout_city(data)
    print "开始markland_test"
    for data in getdata.markland():
        checkpoint.checkout_city(data)
    print "开始metrostation_test"
    for data in getdata.metrostation():
        checkpoint.checkout_city(data)
    print "开始airport_test"
    for data in getdata.airport():
        checkpoint.checkout_city(data)
    print "开始railwaystation_test"
    for data in getdata.railwaystation():
        checkpoint.checkout_city(data)

def province_test():
    print "开始关键字测试+省份"
    print "开始hotel_test"
    for data in getdata.hotel():
        checkpoint.checkout_province(data)
    print "开始markland_test"
    for data in getdata.markland():
        checkpoint.checkout_province(data)
    print "开始metrostation_test"
    for data in getdata.metrostation():
        checkpoint.checkout_province(data)
    print "开始airport_test"
    for data in getdata.airport():
        checkpoint.checkout_province(data)
    print "开始railwaystation_test"
    for data in getdata.railwaystation():
        checkpoint.checkout_province(data)

def district_test():
    print "开始关键字测试+行政区"
    print "开始hotel_test"
    for data in getdata.hotel():
        checkpoint.checkout_district(data)
    print "开始markland_test"
    for data in getdata.markland():
        checkpoint.checkout_district(data)
    print "开始metrostation_test"
    for data in getdata.metrostation():
        checkpoint.checkout_district(data)
    print "开始airport_test"
    for data in getdata.airport():
        checkpoint.checkout_district(data)
    print "开始railwaystation_test"
    for data in getdata.railwaystation():
        checkpoint.checkout_district(data)

def downtown_test():
    print "开始关键字测试+商业区"
    print "开始hotel_test"
    for data in getdata.hotel():
        checkpoint.checkout_downtown(data)
    print "开始markland_test"
    for data in getdata.markland():
        checkpoint.checkout_downtown(data)
    print "开始metrostation_test"
    for data in getdata.metrostation():
        checkpoint.checkout_downtown(data)
    print "开始airport_test"
    for data in getdata.airport():
        checkpoint.checkout_downtown(data)
    print "开始railwaystation_test"
    for data in getdata.railwaystation():
        checkpoint.checkout_downtown(data)