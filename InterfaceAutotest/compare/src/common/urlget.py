__author__ = 'guyh'
import yaml
import os


def urlget(testobj):
    nowcmd = os.getcwd()
    #print nowcmd
    f = file('config/cfg_allsearch/url_config.yaml','r')
    return yaml.load(f)[testobj]

def urlall(url,keyword):
    url = url + "&keyword=keywordvlue&districtid=2&lon=121.35801673&lat=31.22016018"
    url = str(url).replace("keywordvlue",keyword)
    return url

