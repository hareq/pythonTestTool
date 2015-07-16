# -*- coding: UTF-8 -*-
__author__ = 'guyh'
from common.ctrip import logger
import sys
from array import array
from common.trd.httpbase import http
from gs_address.common_landmark import getdata,geturl
import pymssql
import json

reload(sys)
sys.setdefaultencoding('utf-8')
log = logger.logger()

def getfoodvlue(content):
    food = []
    for n in content["data"]:
        if n["type"] == "food":
            food.append(n)
    return food


def findaddddd(db_keyword):
    conn=pymssql.connect(host="hoteldb.fat.qa.nt.ctripcorp.com:55888",database="ArchSearchDB")
    cur=conn.cursor()
    all = []
    sql = "select * from gs_poi (nolock) where address like '%"+db_keyword+"%'"
    cur.execute(sql)
    row = cur.fetchone()
    while row:
        all.append(row)
        row = cur.fetchone()
    conn.close()
    return all



def checkout_base(data):
    #print data
    # try:
        db_cityname = array('u', data[7]).tostring()[::2].decode('gbk')
        db_cityid = data[6]
        db_keyword = data[2]
        url = geturl.geturl(db_cityid,db_keyword)  #此处需要替换
        #log.info(url)

        content = http.getresponse_url(url)
        content = json.loads(content)

        adddd = findaddddd(db_keyword)
        if len(getfoodvlue(content)) == 0:
            if len(adddd) != 0:
                print "关键字为",db_keyword,"联想结果中的food个数为",len(getfoodvlue(content)),"数据库中包含存在个数为",len(findaddddd(db_keyword))
            else:
                print "正确","关键字为",db_keyword,"food个数为",len(getfoodvlue(content))
        else:
            for n in getfoodvlue(content):
                if str(n["districtname"]).find(db_cityname) == -1:
                    print "关键字为",db_keyword,"联想结果所在城市为",n["districtname"],"实际搜索城市为",db_cityname
                if adddd.find(str(n["word"])) == -1:
                    print "关键字为",db_keyword,"结果为",n["word"],"不在数据库中"
                else:
                    print "正确","关键字为",db_keyword,"food个数为",len(getfoodvlue(content))

        # print content

        # if total(content) == "0":#测试total的个数
        #     print "关键字测试","测试total结果错误","测试的keyword为:",db_keyword,"城市为",db_cityname
        # else:
        #     pass
    # except:
    #     pass
