# Editor: aaaasubing
# DevelopmentTime: 2021/4/25 10:09
# 字符串的大小写转换的方法
s = 'hello,python'
a = s.upper()
b = s.lower()
print(a, id(a))  # 内存地址改变，转成大写后会产生一个新的字符串对象
print(s, id(s))
print(b, id(b))  # 同为小写，转换后也会产生新的字符串对象
print(b == s)
print(b is s)  # False

s2 = 'hello,Python'
print(s2.swapcase())

print(s2.title())


