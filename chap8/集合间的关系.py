# Editor: aaaasubing
# DevelopmentTime: 2021/4/24 11:07
# 两个集合是否相等（元素相同就相等）
s = {10, 20, 30, 40}
s1 = {30, 40, 20, 10}
print(s == s1)
print(s != s1)  # 集合中的元素是无序的

# 一个集合是否是另一个集合的子集
s2 = {10, 20, 30, 40, 50, 60}
s3 = {10, 20, 30, 40}
s4 = {10, 20, 90}
print(s3.issubset(s2))
print(s4.issubset(s2))

# 一个集合是否是另一个集合的超集
print(s2.issuperset(s3))
print(s2.issuperset(s4))

# 两个集合是否没有交集
print(s3.isdisjoint(s4))  # 有交集为false
s5 = {100, 200, 300}
print(s3.isdisjoint(s5))  # 没有交集为true


