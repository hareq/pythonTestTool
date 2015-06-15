# -*- coding: UTF-8 -*-

__author__ = 'guyh'
from common.trd import read_excel

file = 'datebasea.xls'
data = read_excel.open_excel(file)
table = data.sheet_by_name('2')
table1 = data.sheet_by_name('1')
aa = []
bb = []
cc = []
dd = []


for row_date in range(0, read_excel.rownum(file,'2')):
    keyword = table.cell(row_date, 0).value
    if "," in str(keyword):
        abc = str(keyword).split(",")
        for n in str(keyword).split(","):
            aa.append(n)
    else :
        aa.append(keyword)

for row_date in range(0, read_excel.rownum(file,'1')):
    keyword = table1.cell(row_date, 0).value
    bb.append(keyword)
    if keyword in aa:
        dd.append(keyword)
    else :
        print keyword
        cc.append(keyword)

print bb
print aa
for c in cc:
    print c
print "no in",cc
print "in",dd
