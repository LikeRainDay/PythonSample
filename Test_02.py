import threading
import time
import _thread

exitFlag=0

class myThread (threading.Thread):  #继承父类threading.Thread
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter
    def run(self): #把要执行的代码到run函数里面，县线程创建后会直接被调用
        print("Starting"+self.name)
        print_time(self.name,self.counter,5)
        print("Exiting"+self.name)
def print_time(threadName,delay,counter):
    while counter:
        if exitFlag:
            _thread.exit()
        time.sleep(delay)
        print("%s:%s" % (threadName,time.ctime(time.time())))
        counter-=1

# 创建新线程
thread1=myThread(1,"Thead-1",1)
thread2=myThread(2,"Thead-2",2)

#开启线程
thread1.start()
thread2.start()

print("Exiting Main Thread")

