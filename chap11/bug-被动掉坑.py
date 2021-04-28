# Editor: aaaasubing
# DevelopmentTime: 2021/4/27 9:28
try:
    a = int(input('请输入第一个整数'))
    b = int(input('请输入第二个整数'))
    res = a / b
    print('结果为：', res)
except ZeroDivisionError:
    print('除数不可以为0')
except ValueError:
    print('不能将字符串转换为数字')
except BaseException as e:
    print(e)
