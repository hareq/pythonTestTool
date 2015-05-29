# -*- coding: UTF-8 -*-
__author__ = 'guyh'
from common.trd import read_excel
import sys

def load_keyword_from_AppTestCase():
    file = 'D:\work\code\searchtestrepository\Allsearch\TestCode\AppTestCase.xls'

    allkeyword = []
    for sheetname in read_excel.sheets_name(file):
        if "CAS015" in sheetname:
            data = read_excel.open_excel(file)
            table = data.sheet_by_name(sheetname)
            reload(sys)
            sys.setdefaultencoding('utf-8')
            for row_date in range(5, read_excel.rownum(file,sheetname)):
                keyword = table.cell(row_date, read_excel.find_colum(file,sheetname,'data')).value
                if keyword == '':
                    pass
                elif "\n" in keyword:
                    for n in str(keyword).split("\n"):
                        if n == "":
                            pass
                        elif "," in keyword:
                            for m in str(keyword).split(","):
                                if m != '':
                                    allkeyword.append(m)
                                else:
                                    pass
                elif "," in keyword:
                    for o in str(keyword).split(","):
                        if o != "":
                            allkeyword.append(o)
                        else:
                            pass

                else:
                    allkeyword.append(keyword)

                reload(sys)
                sys.setdefaultencoding('utf-8')
    return allkeyword


def load_keyword_from_datebase():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    allkeyword = []
    file = 'config\cfg_allsearch\database.xls'
    data = read_excel.open_excel(file)
    table = data.sheet_by_name('all')
    for row_date in range(1, read_excel.rownum(file,'all')):
        keyword = table.cell(row_date, read_excel.find_colum(file,'all','keyword')).value
        allkeyword.append(keyword)
    return allkeyword


