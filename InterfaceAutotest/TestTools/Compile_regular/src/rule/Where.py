__author__ = 'guguyanhua'
import re

def select(rlue,json,n,m):
        wherekey = rlue["p"]["where"].keys()[m]
        wherevlue = rlue["p"]["where"][m][wherekey]
        #if re.match("[a-zA-Z0-9]+\@+[a-zA-Z0-9]+\.+[a-zA-Z]",e) !=None:
        if re.match(wherevlue,json.loads(json)["data"][n][wherekey]) !=None:
        #if json.loads(json)["data"][n][wherekey] == wherevlue:
            Ignorebit = "1"
        else:
            Ignorebit = "0"
        return Ignorebit



