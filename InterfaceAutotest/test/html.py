# -*- coding:utf-8 -*-
__author__ = 'guyh'
import os,sys

html = open('index.html', 'w')
html.write("""
<html>
<head>
  <title>Test</title>
  <style>img{float:left;margin:5px;}</style>
</head>
<body>
""")

files = os.listdir('.')

# # 首先处理文本
# for f in files:
#     if f.lower().endswith('.txt'):
#         fp = open(f)
#         content = fp.read()
#         fp.close()
#         html.write("<p>%s</p>" % content)
#
# # 然后处理图片
# for f in files:
#     if f.lower().endswith('.jpg') or f.lower().endswith('.png'):
#         html.write("<img src='%s' />" % f)

#html.write('</body></html>')
html.close()
