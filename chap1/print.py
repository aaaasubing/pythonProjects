# Editor: aaaasubing
# DevelopmentTime: 2021/4/12 10:11
# 可以输出数字
print(520)

# 字符串
print('hello world')
# 双引号内直接输出

# 含有运算符的表达式，会计算
print(3 + 1)

# 输出在文件中，a+表示以读写功能创建，文件不存在就创建，存在的话就在文件内容后继续追加
# 1所指定的盘符必须存在 2使用file=fp
fp = open('D:/text.txt', 'a+')
print('hello world', file=fp)  # 不用file的话文件里没有东西
fp.close()

# 不进行换行输出（输出内容在一行当中） 用逗号进行分隔
print('hello', 'world', 'Python')

