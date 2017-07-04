#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 进程和线程

# 总结一下就是，多任务的实现有3种方式：
# 多进程模式；
# 多线程模式；
# 多进程+多线程模式。

# 多进程
# Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，
# 但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），
# 然后，分别在父进程和子进程内返回。
# 子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，
# 所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID

# 在python中使用fork创建子进程
import os
# print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
# pid = os.fork()
# if pid == 0:
#   print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#   print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

# multiprocessing - 跨平台多进程模块
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    pass

# if __name__ == '__main__':
#    print('Parent process %s.' % os.getpid())
#    p = Process(target=run_proc, args=('test',))
#    print('Child process will start.')
#    p.start()
#    p.join()
#    print('Child process end.')
'''
output:
Process (5960) start...
Parent process 5960.
Child process will start.
Process (17164) start...
Run child process test (17164)...
Child process end.
join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
'''


# Pool
# 进程池，可批量创建子进程
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s run %0.2f seconds.' % (name, (end - start)))

# if __name__=='__main__':
#    print('Parent process %s.' % os.getpid())
#    p = Pool(4)
#    for i in range(5):
#       p.apply_async(long_time_task,args=(i,)) # 重点
#    print('Waiting for all subprocesses done...')
#    p.close()
#    p.join()
#    print('All subprocesses done.')

# 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()
# 之后就不能继续添加新的Process了。
# 请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，这是因为
# Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统
# 的限制。如果改成：
# p = Pool(5) 就可以同时跑5个进程。
# 由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果。
'''
Process (1124) start...
Parent process 1124.
Child process will start.
Process (3216) start...
Run child process test (3216)...
Child process end.
Parent process 1124.
Waiting for all subprocesses done...
Process (8888) start...
Process (6572) start...
Run task 0 (8888)...
Run task 1 (6572)...
Process (908) start...
Process (7340) start...
Run task 2 (908)...
Run task 3 (7340)...
Task 1 run 0.81 seconds.
Run task 4 (6572)...
Task 2 run 0.99 seconds.
Task 3 run 2.37 seconds.
Task 0 run 2.40 seconds.
Task 4 run 2.32 seconds.
All subprocesses done.
'''

# 子进程
# 很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程
# 的输入和输出。
# subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出

# 在python代码中运行命令nslookup www.python.org
# import subprocess
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)

# 如果子进程还需要输入，则可以通过communicate()方法输入：
# 相当于在命令行执行命令nslookup，然后手动输入：
# set q=mx
# python.org
# exit
import subprocess
# print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8')) # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc8 in position
                                #  2: invalid continuation byte
# print(output) # 不指定反而能输出，略乱，暂不深究
# print('Exit code:', p.returncode)

# 进程间通信
# Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的
# 机制，提供了Queue、Pipes等多种方式来交换数据。
# 以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get('True')
        print('Get %s from queue.' % value)

if __name__=='__main__':
    #父进程创建Queue,并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    #启动子进程pw，写入：
    pw.start()
    #启动子进程pr,读取：
    pr.start()
    #等待pw结束：
    pw.join()
    #pr进程里是死循环，无法等待其结果，只能强行终止：
    pr.terminate()

'''
output:
Process to read: 9516
Process to write: 5788
Put A to queue...
Get A from queue.
Put B to queue...
Get B from queue.
Put C to queue...
Get C from queue.
'''

# 在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。
# 由于Windows没有fork调用，因此，multiprocessing需要“模拟”出fork的效果，父进程所有Python
# 对象都必须通过pickle序列化再传到子进程去，所有，如果multiprocessing在Windows下调用失败了，
# 要先考虑是不是pickle失败了。
