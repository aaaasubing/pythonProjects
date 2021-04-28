# Editor: aaaasubing
# DevelopmentTime: 2021/4/26 19:49
# 形参和实参名字可以不痛
def fun(arg1, arg2):
    print('arg1=', arg1)
    print('arg2=', arg2)
    arg1 = 100
    arg2.append(10)
    print('arg1=', arg1)
    print('arg2=', arg2)
    # return


n1 = 11
n2 = [22, 33, 44]
print('n1=', n1)
print('n2=', n2)
fun(n1, n2)  # 位置传参，arg为形参，n为实参，实参形参可以不同
print('n1=', n1)
print('n2=', n2)

"""
在函数调用过程中，进行参数的传递
如果是不可变对象，在函数体的修改不会影响实参的值   arg1修改为100，不会影响n1的值
如果是可变对象，在函数体内的修改会影响实参的值   arg2的修改，增加10，会影响n2的值，列表是可变对象
"""
