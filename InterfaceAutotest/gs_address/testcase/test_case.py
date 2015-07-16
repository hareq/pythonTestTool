# -*- coding: UTF-8 -*-
__author__ = 'guyh'

from gs_address.common_landmark import getdata,geturl,checkpoint



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
