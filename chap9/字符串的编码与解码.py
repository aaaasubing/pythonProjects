# Editor: aaaasubing
# DevelopmentTime: 2021/4/25 20:24
"""
为什么需要字符串的编码转换：str在内存中以unicode表示，从A计算机到B计算机，需要用byte字节传输
编码：将字符串转换为二进制数据（bytes）
解码：将bytes类型的数据转换为字符串类型
"""
s = '天涯共此时'
# 编码
print(s.encode(encoding='GBK'))  # 在GBK这种编码格式中，一个中文占两个字节
print(s.encode(encoding='UTF-8'))  # 在UTF-8这种编码格式中，一个中文占三个字节

# 解码
# byte代表的是一个二进制数据（字节类型的数据）
byte = s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))  # 编码解码格式必须相同
byte1 = s.encode(encoding='UTF-8')
print(byte1.decode(encoding='UTF-8'))

# 主要在爬虫中应用
