# -*- coding: utf-8 -*-
__author__ = 'guyh'
import xlrd
def open_excel(file):
     try:
         data = xlrd.open_workbook(file)
         return data
     except Exception,e:
         print str(e)

#根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
def excel_table_byindex(file,colnameindex=1,by_index=1):
      data = open_excel(file)
      table = data.sheets()[by_index]
      nrows = table.nrows #行数
      ncols = table.ncols #列数
      colnames =  table.row_values(colnameindex) #某一行数据
      list =[]
      for rownum in range(1,nrows):
           row = table.row_values(rownum)
           if row:
               app = {}
               for i in range(len(colnames)):
                  app[colnames[i]] = row[i]
               list.append(app)
      return list


def excel_table_one_vlue(file,sheet,n,m):
      data = open_excel(file)
      table = data.sheet_by_name(sheet)
      return table.cell(n,m).value


#根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
def excel_table_colnameindex(file,colnameindex=0,by_name='financing'):
     data = open_excel(file)
     table = data.sheet_by_name(by_name)
     nrows = table.nrows #行数
     colnames =  table.row_values(colnameindex) #某一行数据
     list =[]
     for rownum in range(1,nrows):
          row = table.row_values(rownum)
          if row:
              app = {}
              for i in range(len(colnames)):
                 app[colnames[i]] = row[i]
              list.append(app)
     return list


#根据名称获取Excel表格中的数据   参数:file：Excel文件路径     cloname：表头名称  ，sheetname：Sheet1名称

def excel_table_byname(file,sheetname,cloname):
     data = open_excel(file)
     table = data.sheet_by_name(sheetname)
     i = find_colum(file,sheetname,cloname)
     for oo in range(len(table.col_values(i))):
         if table.col_values(i)[oo] == "":
             break
     return table.col_values(i)[1:oo]


def excel_table_onecol(file,sheetname,colnum):
     data = open_excel(file)
     table = data.sheet_by_name(sheetname)
     #print table.cell(1,1).value
     return table.row_values(colnum)


def excel_table_byindex(file,colnameindex=1,by_index=1):
      data = open_excel(file)
      table = data.sheets()[by_index]
      nrows = table.nrows #行数
      ncols = table.ncols #列数
      colnames =  table.row_values(colnameindex) #某一行数据
      list =[]
      for rownum in range(1,nrows):
           row = table.row_values(rownum)
           if row:
               app = {}
               for i in range(len(colnames)):
                  app[colnames[i]] = row[i]
               list.append(app)
      return list


def clonun(file,sheetname,cloname):

    a = len(excel_table_byname(file,sheetname,cloname))
    return a


def rownum(file,sheet):
    data = open_excel(file)
    table = data.sheet_by_name(sheet)
    nrows = table.nrows
    return nrows

def colnum(file,sheet):
    data = open_excel(file)
    table = data.sheet_by_name(sheet)
    ncols = table.ncols
    return ncols

def find_colum(file,sheet,name):
    data = open_excel(file)
    table = data.sheet_by_name(sheet)
    for row in range(0,table.nrows):
        rowValuelist = table.row_values(row)
        if name in rowValuelist:
            colum = rowValuelist.index(name)
            return colum
            #print "%s , %s" % (row, colum)
            #print table.cell(row,colum).value



