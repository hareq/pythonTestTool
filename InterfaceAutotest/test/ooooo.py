__author__ = 'guyh'
str = '"type":"airport"grey}ertert}'
print str
print str.replace('"type":"airport"'+"/w",'')

aaa = open("199.txt","r")
bbb = aaa.read().replace(" ","")
aaa = open("199.txt","w")
aaa.write(bbb)
aaa.close()

ccc = open("241.txt","r")
ddd = ccc.read().replace(" ","")
ccc = open("241.txt","w")
ccc.write(ddd)
ccc.close()



