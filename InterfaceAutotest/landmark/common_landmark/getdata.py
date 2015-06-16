# -*- coding: UTF-8 -*-
__author__ = 'guyh'
import sys
import pymssql
from array import array



def hotel():
    all = []
    conn=pymssql.connect(host="hoteldb.fat.qa.nt.ctripcorp.com:55888",database="ArchSearchDB")
    cur=conn.cursor()

    cur.execute("select top 10000 lat,lon,name,hotelid as id,'hotel' as type,'hotel_' + cast(hotelid as varchar) as identityid,c.*,newid() random from hotel(nolock) left join city(nolock) as c on hotel.cityid=c.cityid where hotel.isdelete=0 and hotel.isoriginal is not null and hotel.isoriginal=1 and countryid = '1' order by random")
    row = cur.fetchone()
    while row:
        all.append(row)
        row = cur.fetchone()
    conn.close()
    return all

def markland():
    all = []
    conn=pymssql.connect(host="hoteldb.fat.qa.nt.ctripcorp.com:55888",database="ArchSearchDB")
    cur=conn.cursor()
    cur.execute("SELECT top 10000 lat,lon,name,marklandid as id,'markland' as type,'markland_' + cast(marklandid as varchar) as identityid,c.* ,newid() random from hotel_markland(nolock) as hm left join city(nolock) as c on hm.cityid=c.cityid where hm.DicationaryType != 'hcz' and DicationaryType != 'jc2' and countryid = '1' order by random")
    row = cur.fetchone()
    while row:
        all.append(row)
        try:
          row = cur.fetchone()
        except:
            pass
    conn.close()
    return all

def metrostation():
    all = []
    conn=pymssql.connect(host="hoteldb.fat.qa.nt.ctripcorp.com:55888",database="ArchSearchDB")
    cur=conn.cursor()
    cur.execute("select top 10000 glat as lat,glon as lon,landmarkname as name,landmarkid as id,'metrostation' as type,'metrostation_' + cast(landmarkid as varchar) as identityid,c.*,newid() random from type_metrostation(nolock) as metro left join city(nolock) as c on metro.city=c.cityid where countryid = '1' order by random")
    row = cur.fetchone()
    while row:
        all.append(row)
        row = cur.fetchone()
    conn.close()
    return all

def airport():
    all = []
    conn=pymssql.connect(host="hoteldb.fat.qa.nt.ctripcorp.com:55888",database="ArchSearchDB")
    cur=conn.cursor()
    cur.execute("SELECT top 10000 lat,lon,name,marklandid as id,'airport' as type,'airport_' + cast(marklandid as varchar) as identityid,c.*,newid() random from hotel_markland(nolock) as hm left join city(nolock) as c on hm.cityid=c.cityid where DicationaryType = 'jc2' and countryid = '1' order by random")
    row = cur.fetchone()
    while row:
        all.append(row)
        row = cur.fetchone()
    conn.close()
    return all

def railwaystation():
    all = []
    conn=pymssql.connect(host="hoteldb.fat.qa.nt.ctripcorp.com:55888",database="ArchSearchDB")
    cur=conn.cursor()
    cur.execute("SELECT top 10000 lat,lon,name,marklandid as id,'railwaystation' as type,'railwaystation_' + cast(marklandid as varchar) as identityid,c.*,newid() random from hotel_markland(nolock) as hm left join city(nolock) as c on hm.cityid=c.cityid where hm.DicationaryType = 'hcz' and countryid = '1' order by random")
    row = cur.fetchone()
    while row:
        all.append(row)
        row = cur.fetchone()
    conn.close()
    return all

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