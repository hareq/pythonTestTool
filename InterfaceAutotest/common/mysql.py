# -*- coding: UTF-8 -*-
__author__ = 'guyh'

import MySQLdb
# try:
print 'bbbb'
conn = MySQLdb.connect(
        host='hoteldb.uat.qa.nt.ctripcorp.com',
        port = 55888,
        user='CN1/guyh',
        passwd='',
        db ='ArchSearchDB',
        )
print 'aaa'
cur = conn.cursor()
# a = cur.execute("select top 10 * from city(nolock)where cityname= '巴黎'")
# print a
# cur.close()
# conn.close()
# # except MySQLdb.Error,e:
# #      print "Mysql Error %d: %s" % (e.args[0], e.args[1])
__author__ = 'guyanhua'

import MySQLdb
try:
    conn= MySQLdb.connect(
        host='192.168.1.48',
        port = 3306,
        user='root',
        passwd='1234',
        db ='vmdai_1124',
        )
    cur=conn.cursor()
    aa = cur.execute('select * from user')
    print "a",aa
    info = cur.fetchmany(aa)
    print info
    for ii in info:
        print ii
    cur.close()
    conn.commit()
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])


