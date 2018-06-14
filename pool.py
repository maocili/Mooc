import threading
import pool_Login as Login
from time import ctime, sleep
# 20172027617	123456
# 20172027618	123456
# 20172027619	123456
def tk1(name):
    head = Login.requests_interface.login('20172027617','123456')
    Login.requests_interface.start('xxdgaeiojkdp4a39rqtp1q')
    print(ctime())

def tk2(code):
    head = Login.requests_interface.login('20172027618','123456')
    Login.requests_interface.start('xxdgaeiojkdp4a39rqtp1q')
    print(ctime())
def tk3(code):
    head = Login.requests_interface.login('20172027619','123456')
    Login.requests_interface.start('xxdgaeiojkdp4a39rqtp1q')
    print(ctime())
threads = []

# 创建了threads数组，创建线程t1,使用threading.Thread()方法，
# 在这个方法中调用music方法target=music，args方法对music进行传参。 把创建好的线程t1装到threads数组中。
# 定义单元素的tuple有歧义，所以 Python 规定，单元素 tuple 要多加一个逗号“,”，这样就避免了歧义：
t1 = threading.Thread(target=tk1, args=(u'伟大的闯爷之歌',))
threads.append(t1)

# 接着以同样的方式创建线程t2，并把t2也装到threads数组。
t2 = threading.Thread(target=tk2, args=(u'python代码',))
threads.append(t2)

t3 = threading.Thread(target=tk3, args=(u'python代码',))
threads.append(t3)

if __name__ == '__main__':
    for t in threads:
        # setDaemon(True)将线程声明为守护线程，必须在start() 方法调用之前设置，如果不设置为守护线程程序会被无限挂起。
        # 子线程启动后，父线程也继续执行下去，
        # 当父线程执行完最后一条语句print "all over %s" %ctime()后，没有等待子线程，直接就退出了，同时子线程也一同结束。
        t.setDaemon(True);
        # 开始线程活动
        t.start()
    t.join()
    print("all over", ctime())