# 错误、调试和测试

# 错误处理
try:
    pass
except Exception as e:
    pass
finally:
    pass


# 调用堆栈
# 记录错误 - log

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e) #同样是出错，但程序打印完错误信息化偶会继续执行，并正常退出

# main()
# print('END')

# 抛出错误 - 本质是 raise 一个 class 实例
# 如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），
# 尽量使用Python内置的错误类型。
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

# 向上抛错误
def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise
def raise_test():
    try:
        10 / 0
    except ZeroDivisionError:
        raise ValueError('input error!') # raise 可以转类型



# 调试 - print, assert, logging, pdb
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!' # python -O err.py  -O 参数可以关闭断言
    return 10 / n

# logging
import logging
logging.basicConfig(level=logging.INFO) # 输出错误信息
# logging允许你指定记录信息的级别，有debug，info，warning，error等几个级别，
# 当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，
# debug和info就不起作用。
# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。

# 单元测试
# 函数abs() - 测试用例：
# 1.    输入正数，比如1、1.2、0.99，期待返回值与输入相同；
# 2.    输入负数，比如-1、-1.2、-0.99，期待返回值与输入相反；
# 3.    输入0，期待返回0；
# 4.    输入非数值类型，比如None、[]、{}，期待抛出TypeError。

# 测试一个类， 例子
# Dict类，这个类的行为和dict一致，但是可以通过属性来访问
# d = Dict(a=1, b=2)
# d['a'] # 1
# d.a # 1
class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s' % key")
    def __setattr__(self, key, value):
        self[key] = value

# 单元测试：
import unittest

# from mydict import Dict

class TestDict(unittest.TestCase): # 测试类，继承子unittest.TestCase
    # 以test开头的方法就是测试方法，不以test开头的方法
    # 不被认为是测试方法，测试的时候不会被执行。
    def test_init(self):
        d = Dict(a = 1, b = 'test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

# 运行测试用例，一般加在 mydict_test.py 最后。
# 命令行运行： python3 -m unittest my_dict.test
# if __name__ == '__main__':
#    unittest.main()

''' output
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
'''

# setup teafdown - 在每个测试方法的前后分别被运行


# 文档测试 - Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。

class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

# 当模块正常导入时，doctest不会被执行。只有在命令行直接运行时，才执行doctest
# ps: 测试了一下命令行运行，没成功
if __name__=='__main__':
    import doctest
    doctest.testmod()