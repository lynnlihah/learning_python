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