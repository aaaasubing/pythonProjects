# Editor: aaaasubing
# DevelopmentTime: 2021/4/19 11:16

a = 1
# 判断条件表达式
while a < 10:
    # 执行条件执行体
    print(a)
    a += 1

# 计算0到4之间的累加和
'''
四步循环法：
1.初始化变量
2.条件判断
3.条件执行体（循环体）
4.改变变量
总结：初始化的变量与条件判断的变量与改变的变量为同一个
'''
b = 0
sum = 0
while b < 5:
    # 循环体
    sum += b
    b += 1
print('和为：', sum)

# 计算1到100之间的偶数和
c = 1
sum1 = 0
while c <= 100:
    if c % 2:  # c % 2 == 0:  # 用到了对象的布尔值
        sum1 += c
    c += 1
print('1到100之间的奇数和：', sum1)

d = 1
sum2 = 0
while d <= 100:
    if d % 2 == 0:
        sum2 += d
    d += 1
print('1到100之间的偶数和：', sum2)

e = 1
sum3 = 0
while e <= 100:
    if not bool(e % 2):  # 用到了对象的布尔值
        sum3 += e
    e += 1
print('1到100之间的偶数和：', sum3)
