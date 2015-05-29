__author__ = 'guyh'
import pymssql


def frommssql():


    frommssql = []

    conn=pymssql.connect(host="hoteldb.uat.qa.nt.ctripcorp.com:55888",database="ArchSearchDB")
    cur=conn.cursor()
    cur.execute("select configs.confkey,configs.confvalue ,indexs.indexName from configs join indexs on configs.sysNo=indexs.sysNo where confkey='rebuild.ip'")
    row = cur.fetchone()
    while row:
        frommssql.append(row[1])
        row = cur.fetchone()
    conn.close()

    conn=pymssql.connect(host="hoteldb.uat.qa.nt.ctripcorp.com:55888",database="ArchSearchDB")
    cur=conn.cursor()
    cur.execute("select configs.confkey,configs.confvalue ,indexs.indexName from configs join indexs on configs.sysNo=indexs.sysNo where confkey='engine.ips'")
    row = cur.fetchone()
    while row:
        frommssql.append(row[1])
        row = cur.fetchone()
    conn.close()

    conn=pymssql.connect(host="hoteldb.fat.qa.nt.ctripcorp.com:55888",database="ArchSearchDB")
    cur=conn.cursor()
    cur.execute("select configs.confkey,configs.confvalue ,indexs.indexName from configs join indexs on configs.sysNo=indexs.sysNo where confkey='rebuild.ip'")
    row = cur.fetchone()
    while row:
        frommssql.append(row[1])
        row = cur.fetchone()
    conn.close()

    conn=pymssql.connect(host="hoteldb.fat.qa.nt.ctripcorp.com:55888",database="ArchSearchDB")
    cur=conn.cursor()
    cur.execute("select configs.confkey,configs.confvalue ,indexs.indexName from configs join indexs on configs.sysNo=indexs.sysNo where confkey='engine.ips'")
    row = cur.fetchone()
    while row:
        frommssql.append(row[1])
        row = cur.fetchone()
    conn.close()

    conn=pymssql.connect(host="hoteldb.lpt.qa.nt.ctripcorp.com:55888",database="ArchSearchDB")
    cur=conn.cursor()
    cur.execute("select configs.confkey,configs.confvalue ,indexs.indexName from configs join indexs on configs.sysNo=indexs.sysNo where confkey='rebuild.ip'")
    row = cur.fetchone()
    while row:
        frommssql.append(row[1])
        row = cur.fetchone()
    conn.close()

    conn=pymssql.connect(host="hoteldb.lpt.qa.nt.ctripcorp.com:55888",database="ArchSearchDB")
    cur=conn.cursor()
    cur.execute("select configs.confkey,configs.confvalue ,indexs.indexName from configs join indexs on configs.sysNo=indexs.sysNo where confkey='engine.ips'")
    row = cur.fetchone()
    while row:
        frommssql.append(row[1])
        row = cur.fetchone()
    conn.close()


    return frommssql


for n in frommssql():
    print n