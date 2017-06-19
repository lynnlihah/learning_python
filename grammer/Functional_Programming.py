#函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数
#高阶函数
#1.变量可以指向函数
f = abs
#print(f)    #<built-in function abs>
f(-10)      #10
#2.函数名也是变量
#运行abs = 10，则会破坏abs()函数
#注：由于abs函数实际上是定义在import builtins模块中的，所以要让修改abs变量的指向在其它模块也生效，
#要用import builtins; builtins.abs = 10
#3.传入函数
#既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。如：
def add(x, y, f):
    return f(x) + f(y)

add(-5, 6, abs)  # x=-5,y=6,f=abs,f(x)=5,f(y)=6 output:11

#map和reduce
#map
def f(x):
    return x * x
r = map(f,[1,2,3,4,5,6,7,8,9]) #f->函数，理解成指定运算规则
list(r) #[1, 4, 9, 16, 25, 36, 49, 64, 81]

#reduce应该是指归纳 -- reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def add(x, y):
    return x + y
reduce(add, [1,3,5,7,9]) #output:25 可以实现累加

#如将[1,3,5,7,9]变成整数13579，就可以：
def fn(x, y):
    return x * 10 + y
reduce(fn, [1,3,5,7,9])
#综合运用
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

str2int('34567') #调用

#用lambda进一步简化成：
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

#filter:和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_odd(n):
    return n % 2 == 1
list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])) #[1, 5, 9, 15]

def not_empty(s):
    return s and s.strip()
list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])) #['A', 'B', 'C']
#注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。

#用filter求素数
#埃氏筛法：取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉；然后去余下数列中的第二个数（3），去倍数，以此类推
#1 构造从3开始的奇数序列：
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
#2 敌营筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0

#3 定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        #print(n)
        pass
    else:
        break

#sorted