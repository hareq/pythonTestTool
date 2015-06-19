# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 19:03:50 2014

@author: yi_liu
"""
import matplotlib.pyplot as plt
import isDigit 


cpu_cores=8
i=0
avgCPUList=[]
avgCPUtimeList=[]

def get_avgCPU(path,filename):
    del avgCPUList[:]
    cpuFile=path+'/'+filename
    avg_cpu_sum=0
    file_object = open(cpuFile)
    try:
        cpu_lines = file_object.readlines( )        
        for cpu_line in cpu_lines:
            fileds_line=cpu_line.split()
            if isDigit.check_isDigit(fileds_line[8]) != 1:
                continue
            else:
                cpu_field=float(fileds_line[8])
                singlcore_cpu=cpu_field/cpu_cores
                avgCPUList.append(singlcore_cpu)
                
        for i in range(len(avgCPUList)):
            avg_cpu_sum=avg_cpu_sum+avgCPUList[i]
         
        avg_cpu=avg_cpu_sum/len(avgCPUList)        
    finally:
        file_object.close( )
    return avg_cpu
        
def get_avgCPUList(path,filename):
    del avgCPUList[:]
    cpuFile=path+'/'+filename
    file_object = open(cpuFile)
    try:
        cpu_lines = file_object.readlines( )        
        for cpu_line in cpu_lines:
            fileds_line=cpu_line.split()
            if isDigit.check_isDigit(fileds_line[8]) != 1:               
                continue
            else:
                cpu_field=float(fileds_line[8])
                singlcore_cpu=cpu_field/cpu_cores
                avgCPUList.append(singlcore_cpu)
    finally:
        file_object.close( )
    return avgCPUList

def draw_avgCPU(avgCPUList,path,filename,savepath):
    # 设置横坐标和纵坐标的名称
    plt.xlabel('time')
    plt.ylabel('avg CPU--%')
    # 图的标题
    plt.title(filename+"- AVG CPU")
    # 要绘制的线的列表
    avgCPU_dataList = avgCPUList
    del avgCPUtimeList[:]
    for i in range(len(avgCPUList)):
        avgCPUtimeList.append(i) 
    # 根据横坐标和纵坐标画Heap线
    avgCPU_line = plt.plot(avgCPUtimeList, avgCPU_dataList)
    # 设置线的颜色宽度等
    plt.setp(avgCPU_line, color='r', linewidth=0.4) 
    plt.grid(True)
    plt.plot(avgCPUtimeList,avgCPU_dataList)   
    plt.savefig(savepath+'/[1]averageCPU_'+filename+'.png', dpi=120)
    plt.show() 
    
   







