import threading
import Danmu
import random
import time
import os
import sys
import datetime
import multiprocessing
from multiprocessing import Process


lock = threading.Lock()


def put_danmu(filename,pos):
    content = None
    lock.acquire()
    try:
        with open(filename, 'r', encoding='gbk') as f:
            danmu_content = f.read().split('\n')
            while '' in danmu_content:
                danmu_content.remove('')
            print(danmu_content,len(danmu_content),pos.value)
        if pos.value < len(danmu_content):
            putIn = danmu_content[int(pos.value):]
            content = ''
            su = min(10, len(putIn))
            print(putIn)
            for i in range(su):
                content = content + putIn[i] + '\n'
            pos.value = pos.value + su
        else:
            start_time = datetime.datetime.now()
            while True:
                end_time = datetime.datetime.now()
                if (end_time-start_time).seconds>=13:
                    sys.exit()

    finally:
        lock.release()
        if content:
            print(content)
            # time.sleep(random.random())
            Danmu.main(content)


def main(filename,pos):
    while True:
        UiThread = threading.Thread(target=put_danmu, args=(filename,pos))
        UiThread.start()
        UiThread.join(timeout=13)


if __name__ == "__main__":
    filename=input('输出数据储存文本位置')
    pos=multiprocessing.Value('d',0)
    p0 = Process(target=main, args=(filename,pos))
    p1 = Process(target=main, args=(filename,pos))
    p2 = Process(target=main, args=(filename,pos))
    p3 = Process(target=main, args=(filename, pos))
    p0.start()
    p0.join(3)
    p1.start()
    p1.join(3)
    p2.start()
    p2.join(3)
    p3.start()
    p3.join()
