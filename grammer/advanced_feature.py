#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#print(L[0:3]) #L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
              #L[:3] 0可以省略
Li = list(range(100))
#print(Li[-10:], Li[:10:2], Li[::5], Li[:])#后10个数;前10个数，每两个取一个;所有数，每5个取一个;原样复制一个list
#tuple，字符串都可以用，返回结果仍是tuple/字符串

#迭代
#dict 的 迭代
d = {'a':1, 'b':2, 'c':3}
for k in d:
    #print('key:', k, 'value:', d[k])
    pass

for v in d.values():
    #print(v)
    pass

for k,v in d.items():
    #print('key:', k, 'value:', v)
    pass

#判断一个对象是否可迭代
from collections import Iterable
isinstance('abc', Iterable)  #true

#使用enumerate函数迭代list（即取出index)
for i, value in enumerate(['A','B','C']):
    #print('index:', i, 'value:', value)
    pass
#同时引用两个变量
for x,y in [(1, 1), (2, 4), (3, 9)]:
    #print('x:', x, 'y:', y)
    pass

#列表生成式
L1 = [x * x for x in range(1, 11)]    #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
L2 = [m + n for m in 'ABC' for n in 'XYZ']   #['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
#使用列表生成式，列出当前目录下的所有文件和目录名
import os
[d for d in os.listdir('../')]  #['.git', '.idea', 'grammer', 'README.md']
#把一个字符串中的所有字符串变成小写
L3 =  ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L3 ])  #['hello', 'world', 'ibm', 'apple']