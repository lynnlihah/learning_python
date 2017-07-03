#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# IO 编程
# 同步异步 - 同步和异步的区别就在于是否等待IO执行的结果
# 由于CPU和内存的速度远远高于外设的速度，所以，在IO编程中，就存在速度严重不匹配的问题。
# 举个例子来说，比如要把100M的数据写入磁盘，CPU输出100M的数据只需要0.01秒，可是磁盘要
# 接收这100M数据可能需要10秒，怎么办呢？有两种办法：
# 第一种是CPU等着，也就是程序暂停执行后续代码，等100M的数据在10秒后写入磁盘，再接着往下执行，
# 这种模式称为同步IO；
# 另一种方法是CPU不等待，只是告诉磁盘，“您老慢慢写，不着急，我接着干别的事去了”，于是，
# 后续代码可以立刻接着执行，这种模式称为异步IO。

# 很明显，使用异步IO来编写程序性能会远远高于同步IO，但是异步IO的缺点是编程模型复杂。想想看，
# 你得知道什么时候通知你“汉堡做好了”，而通知你的方法也各不相同。如果是服务员跑过来找到你，
# 这是回调模式，如果服务员发短信通知你，你就得不停地检查手机，这是轮询模式。总之，异步IO的复
# 杂度远远高于同步IO。

# 本章的IO编程都是同步模式

# 文件读写
# try:
#    f = open('test.txt', 'r')
#    print(f.read())
# finally:
    # if f:
    #   f.close()

# 以上可以简化为：
# with open('test.txt', 'r') as f:
#    print(f.read())

# 可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，
# 调用readlines()一次读取所有内容并按行返回list。

# for line in f.readlines():
#     print(line.strip()) # 把末尾的'\n'删掉

# file-like Object
# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，
# 还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。
# StringIO就是在内存中创建的file-like Object，常用作临时缓冲。

# 二进制文件：f = open('a.jpg', 'rb')
# 读取非UTF-8的文本文件：
# f = open('gbk.txt', 'r', encoding='gbk', errors='ignore')

# 写文件：参数 'w'
'''
from datetime import datetime

with open('test.txt', 'w') as f:
    f.write('今天是 ')
    f.write(datetime.now().strftime('%Y-%m-%d'))

with open('test.txt', 'r') as f:
    s = f.read()
    print('open for read...')
    print(s)

with open('test.txt', 'rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)
'''
'''output
open for read...
今天是 2017-06-30
open as binary for read...
b'\xbd\xf1\xcc\xec\xca\xc7 2017-06-30'
'''

# StringIO和BytesIO
# 很多时候，数据读写不一定是文件，也可以在内存中读写。
# StringIO - 在内存中读写str
from io import StringIO
f = StringIO()
f.write('hello')
# print(f.getvalue()) # 可以print f的内容： hello

# 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
f = StringIO('hello!\nhi\ngoodbye')
while True:
    s = f.readline()
    if s == '':
        break
    # print(s.strip())

'''output
hello!
hi
goodbye
'''

# BytesIO - 二进制数据操作
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
# print(f.getvalue()) # b'\xe4\xb8\xad\xe6\x96\x87'

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read()
# print(f.getvalue()) # b'\xe4\xb8\xad\xe6\x96\x87'


# 操作文件和目录
import os
os.name # 操作系统类型 # nt - 代表Windows系统 posix - 代表 Linux、Unix 或 Mac OS X
# os.uname() # 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。

# 环境变量
os.environ # 查看环境变量
os.environ.get('PATH') # 或者指定环境变量

# 目录操作
os.path.abspath('.') # 查看当前目录的绝对路径
d = os.path.join('e:/','testdir') # 可以自动正确处理不同操作系统下的目录分隔符
# os.mkdir(d) # 创建目录
# os.rmdir(d) # 删除目录
os.path.split('c:/test/file.txt') # output: ('c:/test', 'file.txt')
os.path.splitext('c:/test/file.txt') # output: ('c:/test/file', '.txt') 获取扩展名

# 文件操作
# os.rename('test.txt', 'test.py') # 对文件重命名
# os.remove('test.py') # 删除文件

# 复制文件：不在os模块，shutil模块提供了copyfile()的函数

# 列出当前目录下的所有目录：
[x for x in os.listdir('.') if os.path.isdir(x)]
# 列出所有.py 文件
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']

# 序列化
# 把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之
# 为serialization，marshalling，flattening等等，都是一个意思。
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

import pickle
# 例： 把一个对象序列化并写入文件：
d = dict(name='Bob', age=20, score=99)
pickle.dumps(d) # 把任意对象序列化成一个bytes
# 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，
# 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
d # {'name': 'Bob', 'age': 20, 'score': 99}

# JSON
# 在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为
# JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
# JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。
# JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：
# JSON类型	    Python类型
# {}		    dict
# []		    list
# "string"	    str
# 1234.56		int或float
# true/false	True/False
# null		    None
import json
d = dict(name='Bob', age=20, score=88)
str = json.dumps(d)
# str # {"name": "Bob", "age": 20, "score": 88} 标准json - 类似的，dump()方法可以直接把JSON写入一个file-like Object

# 把json反序列化为Python对象，用loads或者对应的load()方法
json.loads(str) # 由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str与JSON的字符串之间转换。

# json 进阶 - ython的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，
# 比如定义Student类，然后序列化
# dumps 可选参数default就是把任意一个对象变成一个可序列为JSON的对象
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)

def student2dict(std):
    return{
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

json.dumps(s, default=student2dict) # {"name": "Bob", "age": 20, "score": 88}
# 把任意class的实例变为dict
json.dumps(s, default=lambda obj: obj.__dict__)

# 同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，
# 然后，我们传入的object_hook函数负责把dict转换为Student实例：
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str, object_hook=dict2student) # <__main__.Student object at 0x0000000002940668>