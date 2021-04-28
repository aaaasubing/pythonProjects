# Editor: aaaasubing
# DevelopmentTime: 2021/4/26 18:56
def calc(a, b):  # a,b为形式参数，形参，形参的位置是在函数的定义处
    c = a + b
    return c


result = calc(10, 20)  # 10,20是实际参数，实参，位置是在函数调用处
print(result)

res = calc(b=10, a=20)  # 标记了的参数，有变量名，等号左侧变量的名称称为关键字参数
print(res)
