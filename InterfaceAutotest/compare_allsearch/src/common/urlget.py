__author__ = 'guyh'
import yaml
import os
from common.trd import read_excel


def urlget(testobj):
    nowcmd = os.getcwd()
    #print nowcmd
    f = file('config/cfg_allsearch/urlconfig.yaml','r')
    return yaml.load(f)[testobj]

def urlall(url,keyword):
    url = url + "&keyword=keywordvlue&districtid=2&lon=121.35801673&lat=31.22016018"
    url = str(url).replace("keywordvlue",keyword)
    return url

def urlall_with_lonlat(url,keyword):
    urllist = []
    file = 'config/cfg_allsearch/urlconfig.yaml','r'
    data = read_excel.open_excel(file)
    table = data.sheet_by_name("districtid_lon_lat")
    for row_date in range(1, read_excel.rownum(file,"districtid_lon_lat")):
        districtid = table.cell(row_date, read_excel.find_colum(file,"districtid_lon_lat",'districtid')).value
        lon = table.cell(row_date, read_excel.find_colum(file,"districtid_lon_lat",'lon')).value
        lat = table.cell(row_date, read_excel.find_colum(file,"districtid_lon_lat",'lat')).value
        url = url + "&keyword=keywordvlue&districtid=districtidvalue&lon=lonvalue&lat=latvalue"
        url = str(url).replace("keywordvlue",keyword)
        url = str(url).replace("districtidvalue",districtid)
        url = str(url).replace("lonvalue",lon)
        url = str(url).replace("latvalue",lat)
    return url