#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''变量'''

a = 100
b = True
c = 'string'
PI = 3.14159265359     #const 习惯用法，不保证不会变
print(a,b,c,PI)

d1 = 10 / 3     #3.33333333333
d2 = 10 // 3    #3
print(d1, d2)

'''字符串和编码'''
print(ord('A')) #65
print(ord('中')) #20013
print(chr(66)) #B
print(chr(20013)) #中

print('ABC'.encode('ascii')) #b'ABC' 表示bytes类型，每个字符只占用一个字节
print('中文'.encode('utf-8')) #b'\xe4\xb8\xad\xe6\x96\x87'
print(b'ABC'.decode('ascii')) #ABC
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')) #中文
print(len('ABC')) #3
print(len(b'ABC')) #3

print('Hi,%s' % 'python') #Hi,python
print('%.2f' % 3.14159265359) #3.14
print('growth rate: %d%%' % 7) #7% 用%%输出%符号

'''list和tuple'''

