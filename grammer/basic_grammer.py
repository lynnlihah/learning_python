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

#tuple:另一种有序列表。tuple和list非常类似，但是tuple一旦初始化就不能修改
t1 = ('a',) #定义一个元素的tuple要用 , 标明
t2 = ('a', 'b', ['X', 'Y'])
def print_tuple(t):
    t[2][0] = 1 #('a', 'b', [1, 'Y']) 修改了tuple里的list
    #t[1] = 'a' ##TypeError: 'tuple' object does not support item assignment
    print(t)

#条件判断
def print_age(age):
    print('you age is', age)
    if age >= 18:
        print('adult')
    elif age >= 6:
        print('teenager')
    else:
        print('kid')

#循环 - break,continue
#for
def sum_n(n):
    sum = 0
    for x in list(range(n)):    #range(10)生成整数序列 #list()转换成list
        if x == 100:
            continue
        sum += x
    return sum
list(range(10))  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#while
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
    if sum > 1000:
        break

#dict和set
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d.get('Bob')    #75
d['Bob']    #75

#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1,2,3])
s2 = set([2,3,4])
s1 & s2  #{2, 3}
s1 | s2  #{1, 2, 3, 4}
s1.add(5)   #{1, 2, 3, 5}
s1.remove(3)    #{1, 2, 5}

#函数
#1.pass
def fun():
    pass #占位

#2.默认参数必须指向不变对象！例子
def add_end(L=[]):
    L.append('END')
    return L
add_end()    #['END']
add_end()    #['END', 'END']
#正确实现
def add_end_correct(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
add_end_correct()   #['END']
add_end_correct()   #['END']

#3.可变参数：传入参数的个数是可以变化的
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
nums = [1, 2, 3]
calc(*nums)     #*nums表示把nums这个list的所有元素作为可变参数传进去
                #可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple

#4.关键字参数
#关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name,age,**kw):
    print('name:', name, 'age', age, kw )

#person('Michael', 30, city='Beijing', job='Engineer')    #name: Michael age 30 {'city': 'Beijing', 'job': 'Engineer'}
#也可以写成
extra = {'city':'Beijing','job':'Engineer'}
#person('Amy', 30, **extra)

#5.命名关键字参数-希望限制关键字参数的名字
def person_limit(name, age, *, city, job):
    print(name, age, city, job)

#person_limit('Michael', 30, city='Beijing', job='Engineer') #Michael 30 Beijing Engineer

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person_mix(name, age, *args, city, job):
    print(name, age, args, city, job)

#person_mix('Michael', 30, city='Beijing', job='Engineer') #Michael 30 () Beijing Engineer

#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

#递归函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(5))