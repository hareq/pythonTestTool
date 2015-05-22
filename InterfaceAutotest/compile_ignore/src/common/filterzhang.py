# -*- coding: UTF-8 -*-
__author__ = 'ming.zhang'

import re
import sys


def splitSrc(src):
    pattern = re.compile("\{.*?\}",re.S)
    return pattern.finditer(src)

def prepareString(src):
    temp = unicode(src.strip(),  "UTF-8")
    if (temp[0] == '{'):
        temp= temp[1:]
    return temp;

def getPairPattern(regStr):
    temp = regStr.replace("(","SPECIALMARK")
    temp = temp.replace(")","(")
    temp = temp.replace("SPECIALMARK",")")
    temp = "("+temp+")"
    temp = temp.replace("()","")
    return re.compile(temp,re.S)

def filter(src,regStr):
    pattern = re.compile(regStr,re.S)
    pairPattern = getPairPattern(regStr)
    stringLeft=prepareString(src)
    result=[]
    for subSrc in splitSrc(prepareString(src)):
        #print subSrc.group(0)
        matchIterator = pattern.finditer(subSrc.group(0))
        flag = False
        for match in matchIterator:
            fullString = match.group(0)
            temp = pairPattern.match(fullString)
            if (temp):
                # for  group in temp.groups():
                # #	print group
                    # replaceString = replaceString+group
                replaceString=unicode("",  "UTF-8").join(temp.groups())
                #print fullString
                #print replaceString
                stringLeft=stringLeft.replace(fullString,replaceString)
                #print match.groups()
                result.append(match.groups())
                flag=True
    result.append(stringLeft)
    return result


def leftpart(src,regStr):
    return filter(src,regStr)[len(filter(src,regStr))-1]


def ignorepart(src,regStr):
    if len(filter(src,regStr))>2:
        for n in (len(filter(src,regStr))-1):
            pass

#	print result



str1='''{
    "head": {
        "auth": null,
        "errcode": 0
    },
    "data": [
        {
            "word": "巴黎酒店",
            "type": "channelhotelsearch",
            "districtname": "",
            "url": "ctrip://wireless/hotel_oversea_list?c1=20150519&c2=20150520&c3=192&c5=1"
        },
        {
            "word": "Fraser Suites Le Claridge Champs-Elysées paris(巴黎香榭丽舍克拉里奇辉盛套房酒店)",
            "type": "hotel",
            "price": "2493",
            "star": "豪华型",
            "zonename": "香榭丽舍大街-玛德琳 ",
            "districtname": "巴黎",
            "url": "ctrip://wireless/OverseaHotel?hotelDataType=0&checkInDate=20150524&checkOutDate=20150525&hotelId=981517"
        },
        {
            "word": "Shangri-La Hotel, Paris(巴黎香格里拉)",
            "type": "hotel",
            "price": "6213",
            "star": "豪华型",
            "zonename": "特罗卡代罗广场-帕西区 ",
            "districtname": "巴黎",
            "url": "ctrip://wireless/OverseaHotel?hotelDataType=0&checkInDate=20150525&checkOutDate=20150526&hotelId=730333"
        },
        {
            "word": "Mercure Paris Opera Garnier(巴黎加尼叶歌剧院美居酒店)",
            "type": "hotel",
            "price": "811",
            "star": "高档型",
            "zonename": "香榭丽舍大街-玛德琳 ",
            "districtname": "巴黎",
            "url": "ctrip://wireless/OverseaHotel?hotelDataType=0&checkInDate=20150524&checkOutDate=20150525&hotelId=2081471"
        },
        {
            "word": "Hotel Champs Elysees Plaza Paris（巴黎香谢丽舍广场酒店）",
            "type": "hotel",
            "price": "2804",
            "star": "豪华型",
            "zonename": "香榭丽舍大街-玛德琳 ",
            "districtname": "巴黎",
            "url": "ctrip://wireless/OverseaHotel?hotelDataType=0&checkInDate=20150524&checkOutDate=20150525&hotelId=981521"
        },
        {
            "word": "Hotel The Peninsula Paris(巴黎半岛酒店)",
            "type": "hotel",
            "price": "7328",
            "star": "豪华型",
            "zonename": " ",
            "districtname": "巴黎",
            "url": "ctrip://wireless/OverseaHotel?hotelDataType=0&checkInDate=20150524&checkOutDate=20150525&hotelId=1453568"
        },
        {
            "word": "Pullman Paris Tour Eiffel(巴黎埃菲尔铁塔铂尔曼酒店)",
            "type": "hotel",
            "price": "1215",
            "star": "豪华型",
            "zonename": "埃菲尔铁塔-凡尔赛门 ",
            "districtname": "巴黎",
            "url": "ctrip://wireless/OverseaHotel?hotelDataType=0&checkInDate=20150524&checkOutDate=20150525&hotelId=2081163"
        },
        {
            "word": "Holiday Inn Paris Opera Grands Blvds(巴黎歌剧院林荫大道假日酒店)",
            "type": "hotel",
            "price": "893",
            "star": "舒适型",
            "zonename": "歌剧院-交易所 ",
            "districtname": "巴黎",
            "url": "ctrip://wireless/OverseaHotel?hotelDataType=0&checkInDate=20150524&checkOutDate=20150525&hotelId=2080840"
        },
        {
            "word": "Novotel Paris Centre Tour Eiffel(巴黎中心艾菲尔铁塔诺富特酒店)",
            "type": "hotel",
            "price": "808",
            "star": "高档型",
            "zonename": "埃菲尔铁塔-凡尔赛门 ",
            "districtname": "巴黎",
            "url": "ctrip://wireless/OverseaHotel?hotelDataType=0&checkInDate=20150525&checkOutDate=20150526&hotelId=380538"
        },
        {
            "word": "Hotel France Louvre(法国卢浮宫酒店)",
            "type": "hotel",
            "price": "1312",
            "star": "舒适型",
            "zonename": "玛黑区-蓬皮杜艺术中心 ",
            "districtname": "巴黎",
            "url": "ctrip://wireless/OverseaHotel?hotelDataType=0&checkInDate=20150525&checkOutDate=20150526&hotelId=718244"
        },
        {
            "word": "Intercontinental Paris Le Grand(巴黎洲际大酒店)",
            "type": "hotel",
            "price": "1783",
            "star": "豪华型",
            "zonename": "歌剧院-交易所 ",
            "districtname": "巴黎",
            "url": "ctrip://wireless/OverseaHotel?hotelDataType=0&checkInDate=20150524&checkOutDate=20150525&hotelId=2114060"
        },
        {
            "word": "Le Belmont Champs Elysées(贝尔蒙香榭丽舍大街酒店)",
            "type": "hotel",
            "price": "1407",
            "star": "高档型",
            "zonename": "特罗卡代罗广场-帕西区 ",
            "districtname": "巴黎",
            "url": "ctrip://wireless/OverseaHotel?hotelDataType=0&checkInDate=20150525&checkOutDate=20150526&hotelId=717699"
        },
        {
            "word": "Hotel Des Batignolles(巴蒂诺勒酒店)",
            "type": "hotel",
            "price": "574",
            "star": "经济型",
            "zonename": "议会宫-巴蒂诺尔街 ",
            "districtname": "巴黎",
            "url": "ctrip://wireless/OverseaHotel?hotelDataType=0&checkInDate=20150525&checkOutDate=20150526&hotelId=718529"
        },
        {
            "word": "Hyatt Regency Paris Etoile (ex Concorde Lafayette)(凯悦丽晶巴黎艾托尔酒店（前协和拉斐特酒店）)",
            "type": "hotel",
            "price": "1713",
            "star": "高档型",
            "zonename": "议会宫-巴蒂诺尔街 ",
            "districtname": "巴黎",
            "url": "ctrip://wireless/OverseaHotel?hotelDataType=0&checkInDate=20150525&checkOutDate=20150526&hotelId=811670"
        },
        {
            "word": "Huatian Chinagora(华天中国城酒店)",
            "type": "hotel",
            "price": "879",
            "star": "高档型",
            "zonename": " ",
            "districtname": "巴黎",
            "url": "ctrip://wireless/OverseaHotel?hotelDataType=0&checkInDate=20150524&checkOutDate=20150525&hotelId=983720"
        },
        {
            "word": "Le Mathurin(马蒂兰酒店)",
            "type": "hotel",
            "price": "1348",
            "star": "高档型",
            "zonename": "香榭丽舍大街-玛德琳 ",
            "districtname": "巴黎",
            "url": "ctrip://wireless/OverseaHotel?hotelDataType=0&checkInDate=20150525&checkOutDate=20150526&hotelId=730022"
        },
        {
            "word": "ibis Styles Paris Bercy(宜必思尚品巴黎佩西酒店)",
            "type": "hotel",
            "price": "606",
            "star": "舒适型",
            "zonename": " ",
            "districtname": "巴黎",
            "url": "ctrip://wireless/OverseaHotel?hotelDataType=0&checkInDate=20150524&checkOutDate=20150525&hotelId=1565568"
        },
        {
            "word": "Paris Marriott Opera Ambassador Hotel(巴黎大使歌剧院万豪酒店)",
            "type": "hotel",
            "price": "2028",
            "star": "高档型",
            "zonename": "歌剧院-交易所 ",
            "districtname": "巴黎",
            "url": "ctrip://wireless/OverseaHotel?hotelDataType=0&checkInDate=20150525&checkOutDate=20150526&hotelId=602423"
        },
        {
            "word": "Fraser Suites Harmonie Paris La Defense Apartments(巴黎拉德芳斯谐睦辉盛套房酒店)",
            "type": "hotel",
            "price": "1030",
            "star": "豪华型",
            "zonename": "特罗卡代罗广场-帕西区 ",
            "districtname": "巴黎",
            "url": "ctrip://wireless/OverseaHotel?hotelDataType=0&checkInDate=20150524&checkOutDate=20150525&hotelId=981515"
        },
        {
            "word": "Paris Marriott Champs Elysees Hotel(巴黎香榭丽舍万豪酒店)",
            "type": "hotel",
            "price": "3645",
            "star": "豪华型",
            "zonename": "香榭丽舍大街-玛德琳 ",
            "districtname": "巴黎",
            "url": "ctrip://wireless/OverseaHotel?hotelDataType=0&checkInDate=20150524&checkOutDate=20150525&hotelId=1490101"
        },
        {
            "word": "Hotel San Regis(圣瑞吉斯酒店)",
            "type": "hotel",
            "price": "3001",
            "star": "豪华型",
            "zonename": "香榭丽舍大街-玛德琳 ",
            "districtname": "巴黎",
            "url": "ctrip://wireless/OverseaHotel?hotelDataType=0&checkInDate=20150524&checkOutDate=20150525&hotelId=1579133"
        },
        {
            "word": "Crowne Plaza Paris République(巴黎共和国广场皇冠假日酒店)",
            "type": "hotel",
            "price": "1289",
            "star": "高档型",
            "zonename": "巴士底-共和区 ",
            "districtname": "巴黎",
            "url": "ctrip://wireless/OverseaHotel?hotelDataType=0&checkInDate=20150524&checkOutDate=20150525&hotelId=2113281"
        },
        {
            "word": "Campanile Paris 15 - Tour Eiffel(钟楼巴黎15埃菲尔铁塔酒店)",
            "type": "hotel",
            "price": "512",
            "star": "经济型",
            "zonename": "埃菲尔铁塔-凡尔赛门 ",
            "districtname": "巴黎",
            "url": "ctrip://wireless/OverseaHotel?hotelDataType=0&checkInDate=20150524&checkOutDate=20150525&hotelId=1565612"
        },
        {
            "word": "Paris Marriott Rive Gauche Hotel & Conference Center(巴黎左岸万豪酒店及会议中心)",
            "type": "hotel",
            "price": "917",
            "star": "豪华型",
            "zonename": "蒙帕纳斯大楼-奥尔良门 ",
            "districtname": "巴黎",
            "url": "ctrip://wireless/OverseaHotel?hotelDataType=0&checkInDate=20150524&checkOutDate=20150525&hotelId=1490103"
        },
        {
            "word": "Mandarin Oriental Paris(巴黎文华东方酒店)",
            "type": "hotel",
            "price": "5638",
            "star": "豪华型",
            "zonename": "卢浮宫-夏特莱 ",
            "districtname": "巴黎",
            "url": "ctrip://wireless/OverseaHotel?hotelDataType=0&checkInDate=20150524&checkOutDate=20150525&hotelId=986966"
        },
        {
            "word": "Intercontinental Paris Avenue Marceau(巴黎马塞大街洲际酒店)",
            "type": "hotel",
            "price": "1920",
            "star": "豪华型",
            "zonename": "香榭丽舍大街-玛德琳 ",
            "districtname": "巴黎",
            "url": "ctrip://wireless/OverseaHotel?hotelDataType=0&checkInDate=20150524&checkOutDate=20150525&hotelId=2111534"
        },
        {
            "word": "Pullman Paris Montparnasse(巴黎蒙帕纳斯铂尔曼酒店)",
            "type": "hotel",
            "price": "1170",
            "star": "豪华型",
            "zonename": "蒙帕纳斯大楼-奥尔良门 ",
            "districtname": "巴黎",
            "url": "ctrip://wireless/OverseaHotel?hotelDataType=0&checkInDate=20150524&checkOutDate=20150525&hotelId=1526086"
        },
        {
            "word": "Novotel Paris CDG Terminal(巴黎戴高乐机场候机楼诺富特酒店)",
            "type": "hotel",
            "price": "753",
            "star": "高档型",
            "zonename": "戴高乐机场-鲁瓦西地区 ",
            "districtname": "巴黎",
            "url": "ctrip://wireless/OverseaHotel?hotelDataType=0&checkInDate=20150525&checkOutDate=20150526&hotelId=381929"
        },
        {
            "word": "Holiday Inn Paris Gare De L'est(巴黎东站假日酒店)",
            "type": "hotel",
            "price": "813",
            "star": "舒适型",
            "zonename": "巴黎北站 ",
            "districtname": "巴黎",
            "url": "ctrip://wireless/OverseaHotel?hotelDataType=0&checkInDate=20150524&checkOutDate=20150525&hotelId=2105562"
        },
        {
            "word": "Ibis Styles Paris Gare De L'Est Chateau Landon Hotel(巴黎东站兰登城堡宜必思尚品酒店)",
            "type": "hotel",
            "price": "634",
            "star": "舒适型",
            "zonename": " ",
            "districtname": "巴黎",
            "url": "ctrip://wireless/OverseaHotel?hotelDataType=0&checkInDate=20150524&checkOutDate=20150525&hotelId=1579116"
        },
        {
            "word": "Renaissance Paris Arc de Triomphe Hotel(巴黎凯旋门万丽酒店)",
            "type": "hotel",
            "price": "1916",
            "star": "豪华型",
            "zonename": "议会宫-巴蒂诺尔街 ",
            "districtname": "巴黎",
            "url": "ctrip://wireless/OverseaHotel?hotelDataType=0&checkInDate=20150524&checkOutDate=20150525&hotelId=1490105"
        }
    ]
}'''
reg = '"word(.*?),.*?price(.*?),.*?star(.*?),.*?zonename(.*?),.*?districtname(.*?),.*?hotelId=(\d+)'

reload(sys)
sys.setdefaultencoding('utf8')

print len(filter(str1,reg))
a = filter(str1,reg)[30]
print a

f = open('gutest.txt', 'w')
f.write(a)
f.close()