__author__ = 'guyh'

import pymssql

conn=pymssql.connect(host="hoteldb.uat.qa.nt.ctripcorp.com:55888",database="ArchSearchDB")
cur=conn.cursor()
cur.execute("select configs.confkey,configs.confvalue ,indexs.indexName from configs join indexs on configs.sysNo=indexs.sysNo where confkey='rebuild.ip'")
row = cur.fetchone()
while row:
    print row[1]
    row = cur.fetchone()
conn.close()
