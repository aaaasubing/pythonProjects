# Editor: aaaasubing
# DevelopmentTime: 2021/4/25 10:51
# 从前往后比较
print('apple' > 'app')

print(ord('a'), ord('b'))
print('apple' > 'banana')  # 相当于97>98，False
print(ord('刘'))

# ord相反操作chr，获取字符
print(chr(97), chr(98))
print(chr(21016))

"""
== 与 is 的区别
== 比较的是值
is 比较的是id是否相等
"""
a = b = 'Python'
c = 'Python'
print(a == b)
print(b == c)
print(a is b)
print(b is c)
print(id(a))
print(id(b))
print(id(c))  # 指向同一个内存空间，字符串的驻留机制

