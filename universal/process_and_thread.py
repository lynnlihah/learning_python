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
print('Process (%s) start...' % os.getpid())
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

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
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
