__author__ = 'guguyanhua'

from TestTools.Compile.src.rule import Where
class IgnoreVlueRule:
    def __init__(self,rlue):
        self.rlue = rlue

    def execute(self,json):
        rlue = self.rlue
        try:
            for n in range(len(json.loads(json)["data"])):
                for m in range(len(rlue["p"]["where"])):
                    Ignorebit = Where.select(rlue,json,n,m)
                if Ignorebit == "1":
                    for o in range(len(rlue["p"]["ignore"])):
                        ignorekey = rlue["p"]["ignore"].keys()[o]
                        ignorevlue = rlue["p"]["ignore"][o][ignorekey]
                        replacevlue = json.loads(json)["data"][n].pop(ignorekey)
                        json = json.replace(replacevlue,ignorevlue)
                else:
                    pass
        except Exception:
            print Exception
        return json