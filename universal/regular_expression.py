#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = r'ABC\\-001'

import re
# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345')) #<_sre.SRE_Match object; span=(0, 9), match='010-12345'>

test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')

# 用正则切分字符串
print(re.split(r'\s+', 'a b   c')) # ['a', 'b', 'c']
print(re.split(r'[\s\,]+', 'a,b, c  d'))
print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))

# 分组
# 如： ^(\d{3})-(\d{3,8})$分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m) # <_sre.SRE_Match object; span=(0, 9), match='010-12345'>
print(m.group(0)) # 010-12345
print(m.group(1)) # 010
print(m.group(2)) # 12345

# 注意到group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串。

t = '19:05:30' # 直接识别合法的时间
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups()) # ('19', '05', '30')

# 贪婪（尽可能多地匹配）和非贪婪匹配，加？
re.match(r'^(\d+)(0*)$', '102300').groups() # ('102300', '')
re.match(r'^(\d+?)(0*)$', '102300').groups()　# ('1023', '00')


# 当我们在Python中使用正则表达式时，re模块内部会干两件事情：
# 编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
# 用编译后的正则表达式去匹配字符串。
# 为了效率可以预编译

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
re_telephone.match('010-12345').groups()