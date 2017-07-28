#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# hashlib 提供了常见的摘要算法，如MD5，SHA1等等
# 什么是摘要算法呢？摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换
# 为一个长度固定的数据串（通常用16进制的字符串表示）。

# 摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)很容易，但通过
# digest反推data却非常困难。而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同。

import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest()) # d26a53750bc40b38b65a520292f69306

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest()) # 2c76b57293ce30acef38d98f6046927161b46a44