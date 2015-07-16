# -*- coding: UTF-8 -*-
__author__ = 'guyh'

import threading

from compare_ctrip.src.ctrip import all_search_online,all_search_h5,all_search_offline,all_search_app65,all_search_app66,gs_app65,gs_app66,gs_h5
from common.ctrip import logger

log = logger.logger()


#all_search_app.all_search_app()
#all_search_h5.all_search_h5()
#all_search_online.all_search_online()
#gs_app.gs_app()
#gs_online.gs_online()
#all_search_offline.all_search_offline()


threads = []
t1 = threading.Thread(target=all_search_app65.all_search_app65(),args=(u'a',))
threads.append(t1)
t2 = threading.Thread(target=all_search_app66.all_search_app66(),args=(u'b',))
threads.append(t2)
t3 = threading.Thread(target=all_search_online.all_search_online(),args=(u'c',))
threads.append(t3)
t4 = threading.Thread(target=all_search_h5.all_search_h5(),args=(u'd',))
threads.append(t4)
t5 = threading.Thread(target=all_search_offline.all_search_offline(),args=(u'a',))
threads.append(t5)
t6 = threading.Thread(target=gs_app66.gs_app66(),args=(u'b',))
threads.append(t6)
t7 = threading.Thread(target=gs_app65.gs_app65(),args=(u'c',))
threads.append(t7)
t8 = threading.Thread(target=gs_h5.gs_h5(),args=(u'd',))
threads.append(t8)

if __name__ == '__main__':
    for t in threads:
        log.info(t)
        t.setDaemon(True)
        t.start()

