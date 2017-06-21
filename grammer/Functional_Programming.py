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
sorted([36, 5, -12, 9, -21])    #[-21, -12, 5, 9, 36]
sorted([36, 5, -12, 9, -21], key=abs)    #[5, 9, -12, -21, 36] 根据绝对值排序
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)  #['about', 'bob', 'Credit', 'Zoo']忽略大小写排序，
                                                          #其实就是全部转为大写或小写再排序，默认按ASCII
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)#反向,['Zoo', 'Credit', 'bob', 'about']

#返回函数
#高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
#可变参数求和示例。正常：
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
#返回求和函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
#调用
f = lazy_sum(1, 3, 5, 7, 9) #返回求和函数
#print(f) #<function lazy_sum.<locals>.sum at 0x00000000028F9730>
f() #25 调用f时才是求和

#请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
f1 == f2 #False

#闭包
#返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

# f1, f2, f3 = count()
# print (f1(), f2(), f3()) # 9 9 9 原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
#重新创建一个函数用于计算 i * i 会返回1 4 9

#匿名函数 - lambda - 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
def build(x, y):
    return lambda: x * x + y * y

list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

#装饰器 - 假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('2017-06-20')

# now()  #call now(): 2017-06-20
# log 是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处
# 把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
# 由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，
# 于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
# wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。
# 在wrapper()函数内，首先打印日志，再紧接着调用原始函数。

# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')
# now() #execute now(): 2015-3-25
now.__name__ #output: wrapper
# 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，
# 所以，一个完整的decorator的写法如下

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
# 或者针对带参数的decorator：
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# 在面向对象（OOP）的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现，
# 而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。

# 偏函数：functools.partial
# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
int2 = functools.partial(int, base=2) #实际上固定了int()函数的关键字参数base
# 也就是 int2('10010') 相当于： kw = { 'base': 2 } int('10010', **kw)
int2('1000000') #64
# int() - 字符串转整型，默认10进制。base参数可以用于设置转换成8进制or2进制等。使用偏函数，相当于：
def int2(x,base=2):
    return int(x, base)

max2 = functools.partial(max, 10)
#实际上会把10作为*args的一部分自动加到左边，也就是：
max2(5, 6, 7)   #output:10  相当于： args = (10, 5, 6, 7)  max(*args)


