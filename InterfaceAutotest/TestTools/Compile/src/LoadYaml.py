__author__ = 'guyh'
import yaml
from TestTools.Compile.src.rule import IgnoreVlue,IgnoreKey,IgnoreListnum,IgnoreListorder


def loadYaml():
    f = file('config/compileconfig.yaml','r')
    rules = yaml.load(f)["config"]
    rulesobj = []
    for n in range(len(rules)):
        if rules[n]["p"][type] == "ignore_vlue":
            rulesobj.add(IgnoreVlue.IgnoreVlueRule(rules[n]))
        else:
            pass

    #return rules;
loadYaml()