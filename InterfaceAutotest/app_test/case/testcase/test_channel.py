# -*- coding: UTF-8 -*-

__author__ = 'guyh'
import unittest
import sys
from common.ctrip import logger

log = logger.logger()

class Test_channel(unittest.TestCase):
    def channelplane_test(self):
        log.info("before")
        assert 1 == 0
        log.info("after")

    def channelhotel_test(self):
        log.info("before")
        assert 1 == 0
        log.info("after")