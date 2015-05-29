# -*- coding: UTF-8 -*-
__author__ = 'guyh'

import logging,os


def logger():
    logging.basicConfig(filename = os.path.join(os.getcwd(), 'log.txt'),level = logging.INFO, filemode = 'w', format = '%(asctime)s - %(levelname)s: %(message)s')
    log = logging.getLogger('root')
    return log