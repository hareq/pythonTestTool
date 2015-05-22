# -*- coding: UTF-8 -*-
__author__ = 'guyh'

from compile_ignore.src.ctrip import all_search_app,all_search_h5,all_search_online,gs_app,gs_online
import threading
from compile_ignore.src.common import logger

log = logger.logger()


# all_search_app.all_search_app()
# all_search_h5.all_search_h5()
# # all_search_online.all_search_online()
# gs_app.gs_app()
# #gs_online.gs_online()

threads = []
t1 = threading.Thread(target=all_search_app.all_search_app(),args=(u'a',))
threads.append(t1)
t2 = threading.Thread(target=all_search_h5.all_search_h5(),args=(u'b',))
threads.append(t2)
t3 = threading.Thread(target=gs_app.gs_app(),args=(u'c',))
threads.append(t3)

if __name__ == '__main__':
    for t in threads:
        log.info(t)
        t.setDaemon(True)
        t.start()