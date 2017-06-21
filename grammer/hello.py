#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module' #任何模块代码的第一个字符串都被视为模块的文档注释

__author__ = ''

#开始写代码
import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('hello, world!')
    elif len(args) == 2:
        print('hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__': #运行文件本身时的调用，一般用于测试
    test()