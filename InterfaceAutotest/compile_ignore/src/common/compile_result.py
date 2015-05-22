# -*- coding: UTF-8 -*-

__author__ = 'guyh'
import sys
import urllib
import time

from common.trd import read_excel
from common.httpbase import http
from compile_ignore.src.common import filter, loadreg, filewrite
from compile_ignore.src.common import urlget
from compile_ignore.src.common import logger

log = logger.logger()

def compile_result(testobj):
    #print testobj
    file = 'config\cfg_allsearch\datebase.xls'
    data = read_excel.open_excel(file)
    table = data.sheet_by_name('all')
    filename1 = "output"+"\\"+testobj+"error1.txt"
    filename2 = "output"+"\\"+testobj+"error2.txt"
    f1 = open(filename1, 'w')
    f2 = open(filename2, 'w')
    for row_date in range(1, read_excel.rownum(file,'all')):
        keyword = table.cell(row_date, read_excel.find_colum(file,'all','keyword')).value
        reload(sys)
        sys.setdefaultencoding('utf-8')
        keyword = str(keyword)
        keyword_quote = urllib.quote(keyword)

        url1 = urlget.urlget(testobj)["url1"]
        url2 = urlget.urlget(testobj)["url2"]

        url1 = urlget.urlall(url1,keyword_quote)
        url2 = urlget.urlall(url2,keyword_quote)

        content1 = http.getresponse_url(url1)
        content2 = http.getresponse_url(url2)

        for m in loadreg.loadreg():
            content1 = filter.leftpart(content1, m)
            content2 = filter.leftpart(content2, m)
        if content1 == content2:
            log.info(str(url1))
            log.info("正确")
        else:
            log.info(str(url2))
            log.info("错误")

        time.sleep(1)
        filewrite.filewrite(f1,content1,keyword)
        filewrite.filewrite(f2,content2,keyword)


