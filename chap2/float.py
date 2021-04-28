# Editor: aaaasubing
# DevelopmentTime: 2021/4/14 9:14
a = 3.14159
print(a, type(a))
n1 = 1.1
n2 = 2.2
print(n1 + n2)  # 可能出现小数位数不确定的情况
# 解决方法：导入模块decimal

from decimal import Decimal
print(Decimal('1.1') + Decimal('2.2'))

# 存在不准确性
n3 = 2.1
print(n1 + n3)  # 结果正常，二进制底层的问题
