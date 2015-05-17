# -*- coding: utf-8 -*-

import os


def configfile():
    aa = os.getcwd()
    bb = aa.find("http_interface_autotest")
    return aa[0:bb+22+1]+"\Framework\config\config.xml"
