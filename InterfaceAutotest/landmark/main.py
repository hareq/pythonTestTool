# -*- coding: UTF-8 -*-
__author__ = 'guyh'
import threading
from landmark.testcase import test_case
import profile

# print "开始hotel_test"
# test_case.hotel_test()
# print "开始markland_test"
# test_case.markland_test()
# print "开始railwaystation_test"
# test_case.railwaystation_test()
# print "开始airport_test"
# test_case.airport_test()
# print "开始metrostation_test"
# test_case.metrostation_test()


#profile.run("test_case.base_test()")



threads = []
t1 = threading.Thread(target=test_case.base_test(),args=(u'a',))
threads.append(t1)
t2 = threading.Thread(target=test_case.city_test(),args=(u'b',))
threads.append(t2)
t3 = threading.Thread(target=test_case.district_test(),args=(u'c',))
threads.append(t3)
t4 = threading.Thread(target=test_case.downtown_test(),args=(u'd',))
threads.append(t4)
t5 = threading.Thread(target=test_case.province_test(),args=(u'd',))
threads.append(t5)

if __name__ == '__main__':
    for t in threads:
        #log.info(t)
        t.setDaemon(True)
        t.start()