# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 12:24:40 2014

@author: liuyi
"""

import os
import CPU as cpu
import jstat as jstat

def walkpath(sr_path,savepath ):
    for path, dirs, files in os.walk(sr_path):
        for filename in files:
            if filename.startswith("cpu_") and filename.endswith("_log"):
                print "zhaodap"
                avgCPU=cpu.get_avgCPU(path,filename)
                str_avg=str(round(avgCPU,3))+'%'
                avgCPUinfo=filename+"\'s average CPU rate is "+str_avg
                cpuFile=open(savepath+"/[0]avgCPU.TXT",'a')
                cpuFile.write(avgCPUinfo+'\n')
                cpuFile.close()
                print "avgCPU",str_avg
                avgCPUList=cpu.get_avgCPUList(path,filename)
                cpu.draw_avgCPU(avgCPUList,path,filename,savepath)
            elif filename.startswith("jstat_") and filename.endswith(".log"):
                heapList=jstat.get_heapList(path,filename)
                puList=jstat.get_puList(path,filename)
                jstat.draw_Heap(heapList,path,filename,savepath)
                jstat.draw_PU(puList,path,filename,savepath)
            else:
                pass
'''
                
            print "path",path
            print "dir",dirs
            print "filename",filename
walkpath(r'D:/BaiduYunDownload/python/')
'''