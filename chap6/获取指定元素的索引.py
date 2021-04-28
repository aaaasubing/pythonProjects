# Editor: aaaasubing
# DevelopmentTime: 2021/4/21 11:44
lst = ['hello', 'world', 98, 'hello']
print(lst.index('hello'))  # 如果列表中有相同元素，只返回列表中相同元素的第一个元素的索引
# print(list.index('Python'))  # 找不到
# 在指定的start和stop之间进行查找
# print(lst.index('hello', 1, 3))  # 找不到
print(lst.index('hello', 1, 4))
print(lst.index('hello', 0, 4))  # 找第一个
