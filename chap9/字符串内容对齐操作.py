# Editor: aaaasubing
# DevelopmentTime: 2021/4/25 10:15
s = 'hello,Python'

print(s.center(20, '*'))  # 居中对齐，第一个参数是宽度，第二个参数是填充符，默认为空格

print(s.ljust(10, '*'))  # 左对齐
print(s.ljust(10))  # 宽度小于字符串，返回原字符串
print(s.ljust(20))  # 填充符默认为空格

print(s.rjust(20, '*'))  # 右对齐
print(s.rjust(20))  # 填充符默认为空格
print(s.rjust(10))  # 宽度小于字符串，返回原字符串

# 右对齐，左边用0填充，只有一个参数
print(s.zfill(20))
print(s.zfill(10))  # 宽度小于字符串，返回原字符串
print('-8910'.zfill(8))  # 0填在负号之后
