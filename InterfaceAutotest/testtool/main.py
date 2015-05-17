__author__ = 'guguyanhua'

#from yaml to Rules
json = "xyz";
rlues = loadYaml();  # list of Rule

for rule in range(rules):
    json = rule.execute(json)



def loadYaml(yaml):
    #read yaml
    rules = List();

    if(type == ingnore){
        rules.add(IgnoreRUle)
    }else{
        rules.add(ReplaceRule)
    }...

    return rules;


1.loadyaml 方法，解析出来所有的规则，返回规则对象list，for循环规则，if语句将每个不同的规则将参数传给不同规则的构造函数中，返回属于此规则的对象
2.每个处理一个方法，每个规则一个，select一个
3.execute是每个规则里都有的，多态调用他
