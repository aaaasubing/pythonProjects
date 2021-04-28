# Editor: aaaasubing
# DevelopmentTime: 2021/4/27 9:51
try:
    a = int(input('请输入第一个整数'))
    b = int(input('请输入第二个整数'))
    res = a / b
except BaseException as e:
    print('出错了', e)
else:
    print('结果为：', res)

# finally
try:
    a = int(input('请输入第一个整数'))
    b = int(input('请输入第二个整数'))
    res = a / b
except BaseException as e:
    print('出错了')
    print(e)
else:
    print('结果为', res)
finally:
    print('无论是否产生异常，总会被执行的代码')
print('程序结束')
