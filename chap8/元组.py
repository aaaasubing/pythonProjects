# Editor: aaaasubing
# DevelopmentTime: 2021/4/23 17:34

# 不可变序列，可变序列
# 可变序列：列表，字典
lst = [10, 20, 45]
print(id(lst))
lst.append(300)
print(id(lst))  # 内存地址未更改

# 不可变序列：字符串，元组
s = 'hello'
print(id(s))
s = s + 'world'
print(s)
print(id(s))  # 内存地址更改
