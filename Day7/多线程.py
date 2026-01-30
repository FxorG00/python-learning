import time
import threading
# import+模块名
# from 模块名 import 功能
# from 模块名 import *
def sing(msg) :
    while True :
        print(f"我在唱歌，我的信息是{msg}")
        time.sleep(1)
def dance(msg) :
    while True :
        print(f"我在跳舞，我的消息是{msg}")
        time.sleep(1)
if __name__ == '__main__' :
    # 创建线程对象，一个对象就是一个线程
    sing_thread=threading.Thread(target=sing,args=('哈哈哈',))
    # 要传个 tuple，所以一个的时候还要加,
    dance_thread=threading.Thread(target=dance,kwargs={'msg':'嘻嘻嘻'})
    # start
    sing_thread.start()
    dance_thread.start()
