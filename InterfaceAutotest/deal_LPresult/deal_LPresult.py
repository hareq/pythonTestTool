# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 14:39:35 2014

@author: liuyi
"""
import walkpath as wp
import mkdir 

sr_path=r'D:\testresult\diy\geolocator'

def deal_LPresult(sr_path):
    savepath=mkdir.mkdir(sr_path)
    print savepath
    wp.walkpath(sr_path,savepath)
    

deal_LPresult(sr_path)   