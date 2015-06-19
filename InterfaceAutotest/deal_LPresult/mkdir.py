# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 14:16:37 2014

@author: liuyi
"""
import os
import time 

def mkdir(path):
 
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
    tm=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    newpath=path+'/LPresult_figure/LPresult_figure_'+tm
    os.makedirs(newpath)
    print newpath+' 创建成功'
    return newpath
 

# 定义要创建的目录
#mkpath="d:\\qttc\\web1\\"
# 调用函数
#mkdir(mkpath)