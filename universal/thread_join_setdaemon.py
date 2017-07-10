# thread - join() & setDaemon()
# join
# join ()方法：主线程A中，创建了子线程B，并且在主线程A中调用了B.join()，那么，主线
# 程A会在调用的地方等待，直到子线程B完成操作后，才可以接着往下执行，那么在调用这个线
# 程时可以使用被调用线程的join方法。
import threading
import time

class MyThread(threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id = id
    def run(self):
        x = 0
        time.sleep(10)
        print(self.id)

'''
if __name__=='__main__':
    t1 = MyThread(999)
    t1.start()
    for i in range(5):
        print(i)
'''
''' 不使用join,output:
0
1
2
3
4
999 
主线程启动了t1之后，继续运行for循环，而t1等等了10秒才打印id 999
'''
'''
if __name__=='__main__':
    t1 = MyThread(999)
    t1.start()
    t1.join()
    for i in range(5):
        print(i)

'''
'''
999 -- 等子线程执行完，主线程才继续运行
0
1
2
3
4
'''

# setDaemon
# setDaemon()方法。主线程A中，创建了子线程B，并且在主线程A中调用了B.setDaemon(),
# 这个的意思是，把主线程A设置为守护线程，这时候，要是主线程A执行结束了，就不管子线程
# B是否完成,一并和主线程A退出.这就是setDaemon方法的含义，这基本和join是相反的。
# 此外，还有个要特别注意的：必须在start() 方法调用之前设置，如果不设置为守护线程
# ，程序会被无限挂起。例子：就是设置子线程随主线程的结束而结束：

class MyThread(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)

    def run(self):

        for i in range(100):
            time.sleep(1)
            print("This is " + self.getName())
            print(i)

if __name__ == '__main__':
    t1 = MyThread(999)
    t1.setDaemon(True)
    t1.start()
    time.sleep(5)
    print("I am the father thread.")

'''  output: 子线程不会完全执行完，就退出了
This is Thread-1
0
This is Thread-1
1
This is Thread-1
2
This is Thread-1
3
I am the father thread.
'''

'''
程序运行中，执行一个主线程，如果主线程又创建一个子线程，主线程和子线程就
分兵两路，分别运行，那么当主线程完成想退出时，会检验子线程是否完成。如果
子线程未完成，则主线程会等待子线程完成后再退出。但是有时候我们需要的是，只
要主线程完成了，不管子线程是否完成，都要和主线程一起退出，这时就可以用
setDaemon方法了。
'''