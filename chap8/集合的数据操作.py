# Editor: aaaasubing
# DevelopmentTime: 2021/4/24 17:43
# 集合的数学操作
# 1.交集
s1 = {10, 20, 30, 40}
s2 = {20, 30, 40, 50, 60}
print(s1.intersection(s2))
print(s1 & s2)  # intersection与&等价，交集操作，s1与s2未发生变化

# 2.并集
print(s1.union(s2))  # 去除重复元素
print(s1 | s2)  # union与|等价，并集操作，s1与s2未发生变化

# 3.差集
print(s1.difference(s2))
print(s1 - s2)  # difference与-等价，差集操作，s1与s2未发生变化

# 4.对称差集
print(s1.symmetric_difference(s2))
print(s1 ^ s2)



