# Editor: aaaasubing
# DevelopmentTime: 2021/4/30 9:12
"""
文件的读写原理：IO操作
队列先进先出
.py文件到解释器，到os，再到硬盘中操作
步骤：打开或新建文件，读写文件，关闭资源
"""
file = open('a.txt', 'r')  # r表示读取
print(file.readlines())  # 结果是个列表，所有内容行
file.close()

