#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3]) #L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
              #L[:3] 0可以省略
Li = list(range(100))
print(Li[-10:], Li[:10:2], Li[::5], Li[:])#后10个数;前10个数，每两个取一个;所有数，每5个取一个;原样复制一个list
#tuple，字符串都可以用，返回结果仍是tuple/字符串

#迭代