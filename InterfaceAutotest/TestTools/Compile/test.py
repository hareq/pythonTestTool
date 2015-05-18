__author__ = 'guyh'
import yaml

def loadYaml():
    f = file('config/compileconfig.yaml','r')
    rules = yaml.load(f)["config"]
    for n in range(len(rules)):
        if rules[n]["p"]["type"] == "ignore_vlue":
            print "a",n
            print rules[n]["p"]["where"].keys()[0]
            #rules.add(IgnoreRUle)
        else :
            print "b",n

    #return rules;
loadYaml()