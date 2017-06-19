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
[s.lower() for s in L3 ]  #['hello', 'world', 'ibm', 'apple']

#生成器
#一边循环一边计算的机制，称为生成器：generator
#1. 把一个列表生成式的[]改成()，就创建了一个generator
g = (x * x for x in range(10))
g    #<generator object <genexpr> at 0x0000000002851F10>
next(g)  #0
next(g)  #1 --- generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
for n in (g):
    #print(n) #迭代g
    pass
#2. yield -- generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
# 斐波拉契数列 -- 打印
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

#改写成generator
def fib_1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib_1(6) #f 是一个 generator

while True:
    try:
        x = next(f)
        #print('f:', x)
        pass
    except StopIteration as e:
        #print('Generator return value:', e.value) #但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
                                                  #如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
        pass
        break

#理解yield的用法
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
o = odd()
'''print(next(o))
print(next(o))
print(next(o))
print(next(o))  # 报错'''

#迭代器
#我们已经知道，可以直接作用于for循环的数据类型有以下几种：
#一类是集合数据类型，如list、tuple、dict、set、str等；
#一类是generator，包括生成器和带yield的generator function。
#这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
#可以使用isinstance()判断一个对象是否是Iterable对象
isinstance([], Iterable) # True
#而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。
#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
#可以使用isinstance()判断一个对象是否是Iterator对象：
from collections import Iterator
isinstance((x for x in range(10)), Iterator) #True

#生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
#把list、dict、str等Iterable变成Iterator可以使用iter()函数：
isinstance(iter([]),Iterator) #True
isinstance([],Iterator) #False
#可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。