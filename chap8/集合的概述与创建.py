# Editor: aaaasubing
# DevelopmentTime: 2021/4/24 9:20
# 集合是没有value的字典，是可变类型（列表、字典）
# 集合中的元素是无序的，不允许重复元素
# 集合的创建方式
# 第一种：使用{}
s = {2, 3, 4, 5, 5, 6, 7, 8}  # 集合中的元素不允许重复
print(s)
# 第二种：使用内置函数set()
s1 = set(range(6))
print(s1, type(s1))
s2 = set([1, 2, 4, 5, 5, 6, 6])  # 去掉了重复元素
print(s2, type(s2))
s3 = set((1, 2, 3, 4, 4, 5, 65))  # 元组类型的元素通过set转为集合元素
print(s3, type(s3))
s4 = set('Python')  # 字符串类型的元素通过set转为集合元素
print(s4, type(s4))  # 无序，且变为一个一个的字母
s5 = set({1, 2, 4, 4, 6})
print(s5, type(s5))
# 空集合的定义
s6 = {}  # dict字典类型
print(type(s6))
s7 = set()
print(s7, type(s7))
