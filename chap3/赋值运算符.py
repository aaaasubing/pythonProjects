# Editor: aaaasubing
# DevelopmentTime: 2021/4/15 20:16
# 赋值运算符，执行顺序：从右到左
i = 3 + 4
print(i)

# 链式赋值
a = b = c = 20
print(a, id(a))  # id为内存地址，三个变量指向相同的地址
print(b, id(b))
print(c, id(c))

# 参数赋值
a = 20
a += 30  # a=a+30
print(a)
a -= 10
print(a)  # a=a-10
a *= 2
print(a)  # a=a*2
print(type(a))  # int
a /= 3
print(a)
print(type(a))  # float
a //= 2
print(a)  # float
a %= 3
print(a)

# 系列解包赋值，要求等号左右数量相同，注意顺序不能错
a, b, c = 20, 30, 40
print(a, b, c)
# 解包赋值应用在交换两个变量的值，不需要中间变量
a, b = 10, 20
print('交换之前：', a, b)
a, b = b, a  # 交换
print('交换之后：', a, b)
