# -*- coding: UTF-8 -*-
__author__ = 'guyh'

from compare_allsearch.src.ctrip import all_search_app,all_search_h5,all_search_online,gs_app,gs_online,all_search_offline
import threading
from compare_allsearch.src.common import logger
import sys
log = logger.logger()


#all_search_app.all_search_app()
#all_search_h5.all_search_h5()
#all_search_online.all_search_online()
#gs_app.gs_app()
#gs_online.gs_online()
#all_search_offline.all_search_offline()


threads = []
t1 = threading.Thread(target=all_search_app.all_search_app(),args=(u'a',))
threads.append(t1)
t2 = threading.Thread(target=all_search_h5.all_search_h5(),args=(u'b',))
threads.append(t2)
t3 = threading.Thread(target=all_search_online.all_search_online(),args=(u'c',))
threads.append(t3)
t4 = threading.Thread(target=gs_app.gs_app(),args=(u'd',))
threads.append(t4)

if __name__ == '__main__':
    for t in threads:
        log.info(t)
        t.setDaemon(True)
        t.start()

