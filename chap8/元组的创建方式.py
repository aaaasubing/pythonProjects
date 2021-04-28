# Editor: aaaasubing
# DevelopmentTime: 2021/4/23 17:37
# 第一种，使用()
t = ('Python', 'world', 98)
print(t)
print(type(t))
t2 = 'Python', 'world', 98  # ()可以省略
print(t2)
print(type(t2))
t3 = ('Python',)  # 只包含一个元组的元素需要使用逗号和小括号，不然会以为是string类型
print(t3)
print(type(t3))

# 第二种，使用内置函数tuple()
t1 = tuple(('Python', 'world', 98))
print(t1)
print(type(t1))

# 空元组的创建方式
t4 = ()
t5 = tuple()
print('空元组：', t4, t5)
# 空列表的创建方式
lst = []
lst1 = list()
print('空列表：', lst, lst1)
# 空字典的创建方式
d = {}
d1 = dict()
print('空字典：', d, d1)

