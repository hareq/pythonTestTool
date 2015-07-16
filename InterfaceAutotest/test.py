__author__ = 'guyh'
try:
    x = 3
    y = 0
    print x/y
except Exception,a:
    print a
print callable(getattr(x/y))