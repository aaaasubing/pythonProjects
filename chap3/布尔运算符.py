# Editor: aaaasubing
# DevelopmentTime: 2021/4/16 11:03
a, b = 1, 2

# and 并且
print(a == b and b == 2)  # True and True ---> True
print(a == 1 and b < 2)  # False
print(a != 1 and b == 2)  # False
print(a !=1 and b != 2)  # False

# or 或者
print(a == 1 or b == 2)  # T
print(a == 1 or b < 2)  # T
print(a != 1 or b == 2)  # T
print(a != 1 or b != 2)  # F

# not 取反，针对bool类型操作数
f = True
ff = False
print(not f)  # F
print(not ff)  # T

# in
# not in
s = 'helloworld'
print('w' in s)
print('k' in s)
print('w' not in s)
print('k' not in s)
