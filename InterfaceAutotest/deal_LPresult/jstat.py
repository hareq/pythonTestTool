# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 16:42:32 2014

@author: liuyi
"""
import matplotlib.pyplot as plt


i=1
heapList=[]
PUList=[]
HeaptimeList = []
PUtimeList=[]
heap=0

def get_heapList(path,filename):
    del heapList[:]
    jstatFile=path+'/'+filename
    file_object = open(jstatFile)
    try:
        jstat_lines = file_object.readlines( )
        for i in range(1,len(jstat_lines)):
            jstat_line= jstat_lines[i].split()
            heap=float(jstat_line[2])+float(jstat_line[3])+\
                 float(jstat_line[5])+float(jstat_line[7])
            heapList.append(heap)
    finally:
        file_object.close( )
    return heapList
        
def get_puList(path,filename):
    del PUList[:]
    jstatFile=path+'/'+filename
    file_object = open(jstatFile)
    try:
        jstat_lines = file_object.readlines( )
        for i in range(1,len(jstat_lines)):
            jstat_line= jstat_lines[i].split()
            pu=float(jstat_line[9])
            PUList.append(pu)        
    finally:
        file_object.close( )
    return PUList
    
def draw_Heap(heapList,path,filename,savepath):
    # 设置横坐标和纵坐标的名称
    plt.xlabel('time')
    plt.ylabel('Heap')
    # 图的标题
    plt.title(filename+"-Heap")
    # 要绘制的线的列表
    heap_dataList = heapList
    del HeaptimeList[:]
    for i in range(len(heapList)):
        HeaptimeList.append(i) 
    # 根据横坐标和纵坐标画Heap线
    heap_line = plt.plot(HeaptimeList, heap_dataList)
    # 设置线的颜色宽度等
    plt.setp(heap_line, color='r', linewidth=0.4) 
    plt.grid(True)
    plt.plot(HeaptimeList,heap_dataList)   
    plt.savefig(savepath+'/[2]Heap_'+filename+'.png', dpi=120)
    plt.show()
    
def draw_PU(PU_array,path,filename,savepath):
    # 设置横坐标和纵坐标的名称
    plt.xlabel('time')
    plt.ylabel('PU')
    # 图的标题
    plt.title(filename+"-PU")
    # 要绘制的线的列表
    PU_dataList = PUList    
    del PUtimeList[:]
    for i in range(len(heapList)):
        PUtimeList.append(i) 
    # 根据横坐标和纵坐标画PU线
    PU_line = plt.plot(PUtimeList, PU_dataList)
    # 设置线的颜色宽度等
    plt.setp(PU_line, color='r', linewidth=0.4) 
    plt.grid(True)
    plt.plot(PUtimeList,PU_dataList)
    plt.savefig(savepath+'/[3]PU_'+filename+'.png', dpi=120)
    plt.show()    
'''
if __name__ == '__main__':
    get_heapList('D:/BaiduYunDownload/python/1/','jstat_1_141117192837.log')
    get_puList('D:/BaiduYunDownload/python/1/','jstat_1_141117192837.log')
    draw_Heap(heapList,'D:/BaiduYunDownload/python/1/','jstat_1_141117192837.log')
    draw_PU(PUList,'D:/BaiduYunDownload/python/1/','jstat_1_141117192837.log')
'''