# Editor: aaaasubing
# DevelopmentTime: 2021/4/25 19:56
# %占位符
name = '张三'
age = 20
print('我叫%s，今年%d岁' % (name, age))

# {}占位符
print('我叫{0}，今年{1}岁'.format(name, age))

# f-string
print(f'我叫{name}，今年{age}岁')

print('%d' % 99)
print('%10d' % 99)  # 10为宽度
print('hellohello')
print('%f' % 3.1415926)
print('%.3f' % 3.1415926)
print('%10.3f' % 3.1415926)  # 同时表示宽度和精度，总宽度为10，小数点后3位
print('hellohello')

print('{}'.format(3.1415926))
print('{0}'.format(3.1415926))  # 最好写上数字
print('{0:.3}'.format(3.1415926))  # .3表示一共三位数字
print('{0:.3f}'.format(3.1415926))  # .3f表示三位小数
print('{:.3f}'.format(3.1415926))
print('{:10.3f}'.format(3.1415926))  # 10表示宽度，.3f表示三位小数，同时表示宽度和精度

