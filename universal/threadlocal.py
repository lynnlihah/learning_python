#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ThreadLocal
# 在多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全
# 局变量好，因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量的修改必须加锁。
# 1 这样导致局部变量在函数调用的时候，传递起来很麻烦
# 2 一个简单粗暴的方案：设置一个全局dict存放所有的Student对象，然后以thread
#   自身作为key获得线程对应的Student对象：
global_dict = {}
def std_thread(name):
    std = Student(name)
    global_dict[threading.current_thread()] = std
    do_task_1()
    do_task_2()

def do_task_1():
    # 不传入std，而是根据当前线程查找：
    std = global_dict[threading.current_thread()]
    pass

def do_task_2():
    # 任何函数都可以查找出当前线程的std变量：
    std = global_dict[threading.current_thread()]
    pass

# 这种方式理论上是可行的，它最大的优点是消除了std对象在每层函数中的传递问题，但
# 是，每个函数获取std的代码有点丑。 ThreadLocal - 自动完成这件事

import threading
# 创建全局ThreadLocal对象
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student：
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

# Hello, Alice (in Thread-A)
# Hello, Bob (in Thread-B)