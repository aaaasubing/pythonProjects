# Editor: aaaasubing
# DevelopmentTime: 2021/4/15 21:03
# 比较运算符，结果为bool类型
a, b = 10, 20
print('a>b吗？', a > b)  # False
print('a<b吗？', a < b)  # True
print('a>=b吗？', a >= b)  # False
print('a<=b吗？', a <= b)  # True
print('a==b吗？', a == b)  # False
print('a!=b吗？', a != b)  # True

# 一个=为赋值，两个==为比较
# 一个变量由三个部分组成，标识，类型，值
# ==比较的是值，比较对象的标识使用is
a = 10
b = 10
print(a == b)  # True，说明a与b的value同
print(a is b)  # True，说明a与b的id同
# 内存赋值时去内存里找有没有这个对象，有的话就不重新创建，给变量相同id即可
lst1 = [11, 22, 33, 44]
lst2 = [11, 22, 33, 44]
print(lst1 == lst2)  # True
print(lst1 is lst2)  # False
print(id(lst1))
print(id(lst2))

# is not 不同为Ture
print(a is not b)  # False，a的id与b同
print(lst1 is not b)  # True
