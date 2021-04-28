# Editor: aaaasubing
# DevelopmentTime: 2021/4/23 19:43
t = ('Python', 'world', 98)
# 第一种获取元组元素的方式，索引
# 需要已知元素有多少
print(t[0])
print(t[1])
print(t[2])
# print(t[3])  # IndexError: tuple index out of range
# 遍历元组
for item in t:
    print(item)
