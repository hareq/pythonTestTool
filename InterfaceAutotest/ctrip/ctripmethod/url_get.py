# -*- coding: utf-8 -*-
__author__ = 'guyh'
import sys

from base.trd import read_excel, china_decode


def get_url(file,sheet,row):
   table = read_excel.open_excel(file).sheet_by_name(sheet)
   a1 = 'http://'
   a2 = str(table.cell(row, read_excel.find_colum(file,sheet,'ipport')).value)
   a3 ='/appautocomplete/search?'

   reload(sys)
   b = table.cell(row, read_excel.find_colum(file,sheet,'keyword')).value
   reload(sys)
   sys.setdefaultencoding('utf-8')
   b = str(b)
   a4 = 'keyword='+ china_decode.chinese_decode(b)
   a5 = 'action='+str(table.cell(row, read_excel.find_colum(file,sheet,'action')).value)
   a6 = 'source'+str(table.cell(row, read_excel.find_colum(file,sheet,'source')).value)
   a7 = 'districtid'+str(table.cell(row, read_excel.find_colum(file,sheet,'districtid')).value)
   url = str(a1+a2+a3+a4+'&'+a5+'&'+a6+'&'+a7)
   return url




