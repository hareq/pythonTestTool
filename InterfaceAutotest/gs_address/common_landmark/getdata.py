# -*- coding: UTF-8 -*-
__author__ = 'guyh'
import sys
import pymssql
from array import array


def get_db_district(cityid):
    conn=pymssql.connect(host="hoteldb.fat.qa.nt.ctripcorp.com:55888",database="ArchSearchDB")
    cur=conn.cursor()
    sql = "select top 1 * from type_location where cityid = "+str(cityid)
    cur.execute(sql)
    row = cur.fetchone()
    conn.close()
    district_name = array('u', row[1]).tostring()[::2].decode('gbk')
    return district_name

def get_db_downtown(cityid):
    conn=pymssql.connect(host="hoteldb.fat.qa.nt.ctripcorp.com:55888",database="ArchSearchDB")
    cur=conn.cursor()
    sql = "select top 1  * from type_zone where cityid = "+str(cityid)
    cur.execute(sql)
    row = cur.fetchone()
    conn.close()
    downtown_name = array('u', row[1]).tostring()[::2].decode('gbk')
    return downtown_name


# for n in hotel():
#     print array('u', n[7]).tostring()[::2].decode('gbk')
#     print n[2]




#db_cityname = array('u', data[7]).tostring()[::2].decode('gbk')