# -*- coding: UTF-8 -*-
__author__ = 'guguyanhua'

from TestTools.Compile_rule.src.rule import Where
import json


class IgnoreVlueRule:
    def __init__(self,rlue):
        self.rlue = rlue

    def execute(self,json):
        rlue = self.rlue
        print json
        # try:
        for n in range(len(json.loads(json)["data"])):
            Ignorebit == ""
            for m in range(len(rlue["p"]["where"])):
                Ignorebit = Where.select(rlue,json,n,m)
                if Ignorebit == "0":
                    break
            if Ignorebit == "1":
                for o in range(len(rlue["p"]["ignore"])):
                    ignorekey = rlue["p"]["ignore"].keys()[o]
                    ignorevlue = rlue["p"]["ignore"][o][ignorekey]
                    replacevlue = json.loads(json)["data"][n].pop(ignorekey)
                    json = json.replace(replacevlue,ignorevlue)
            else:
                pass
        # except Exception:
        #     print Exception,"IgnoreVlueRule"
        return json