#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''变量'''
def variable():
    a = 100; b = True; c = 'string'
    PI = 3.14159265359  #const 习惯用法，不保证不会变
    print(a,b,c,PI)

def division():
    d1 = 10 / 3  #3.33333333333
    d2 = 10 // 3    #3
    print(d1, d2)

'''字符串和编码'''
def str_and_encode():
    print(ord('A'))     #65
    print(ord('中'))     #20013
    print(chr(66))    #B
    print(chr(20013))   #中

    print('ABC'.encode('ascii'))    #b'ABC' 表示bytes类型，每个字符只占用一个字节
    print('中文'.encode('utf-8'))     #b'\xe4\xb8\xad\xe6\x96\x87'
    print(b'ABC'.decode('ascii'))   #ABC
    print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))  #中文
    print(len('ABC'))   #3
    print(len(b'ABC'))  #3

def format_output():
    print('Hi,%s' % 'python')   #Hi,python
    print('%.2f' % 3.14159265359)   #3.14
    print('growth rate: %d%%' % 7)  #7% 用%%输出%符号


'''list和tuple'''
#list
classmates = ['Micheal', 'Bob', 'Tracy']
def print_list(cl):
    print(cl)
    print(cl[0],cl[1],cl[2],cl[-1])
    print(cl.insert(1,'Jack'),cl)   #None ['Micheal', 'Jack', 'Bob', 'Tracy']
    print(cl.pop(),cl)  #Tracy ['Micheal', 'Jack', 'Bob']
    cl[1] = 123; print(cl)   #['Micheal', 123, 'Bob']

#print_list(classmates)

#tuple:另一种有序列表。tuple和list非常类似，但是tuple一旦初始化就不能修改
t1 = ('a',) #定义一个元素的tuple要用 , 标明
t2 = ('a', 'b', ['X', 'Y'])
def print_tuple(t):
    t[2][0] = 1 #('a', 'b', [1, 'Y']) 修改了tuple里的list
    #t[1] = 'a' ##TypeError: 'tuple' object does not support item assignment
    print(t)
print_tuple(t2)


