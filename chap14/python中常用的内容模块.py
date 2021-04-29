# Editor: aaaasubing
# DevelopmentTime: 2021/4/29 18:29
import sys
import time
import urllib.request
import math
import schedule

print(sys.getsizeof(24))
print(sys.getsizeof(45))
print(sys.getsizeof(True))
print(sys.getsizeof(False))

print(time.time())  # 秒
print(time.localtime(time.time()))  # 现在的时间

print(urllib.request.urlopen('http://www.baidu.com').read())  # 爬虫

print(math.pi)


def job():
    print('哈哈')


schedule.every(3).seconds.do(job())  # 三秒执行一次
while True:
    schedule.run_pending()
    time.sleep(1)  # 休眠一秒
