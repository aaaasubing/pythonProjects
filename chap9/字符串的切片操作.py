# Editor: aaaasubing
# DevelopmentTime: 2021/4/25 19:32
s = 'hello,Python'
s1 = s[:5]  # 由于没有指定起始位置，从0开始切
print(s1)
s2 = s[6:]  # 指定起始位置未指定结束位置，切到结束
print(s2)
s3 = '!'
new_str = s1 + s3 + s2
print(new_str)

# id都不同
print(id(s))
print(id(s1))
print(id(s2))
print(id(s3))
print(id(new_str))

# 完整写法：[start:end:step]
print(s[1:5:1])  # 从1开始切到5，不包括5，步长为1
print(s[::2])  # 0246，步长为间隔，默认从开始到结束，步长为2
print(s[::-1])  # 倒置，默认从字符串的最后一个到第一个，因为步长为负数
print(s[-6::1])
