# Editor: aaaasubing
# DevelopmentTime: 2021/4/25 10:28
s = 'hello,Python'

# 判断字符串是否合法
print('1.', s.isidentifier())  # 合法：字母数字下划线
print('2.', 'hello'.isidentifier())
print('3.', '张三_'.isidentifier())
print('4.', '张三_123'.isidentifier())

# 判断字符串是否全部由空白字符组成（回车、换行、水平制表符）
print('5.', '\t'.isspace())

# 判断字符串是否全部由字母组成
print('6.', 'abc'.isalpha())
print('7.', '张三'.isalpha())
print('8.', '张三1'.isalpha())

# 判断字符串是否全部由十进制的数字组成
print('9.', '123'.isdecimal())
print('10.', '123四'.isdecimal())
print('11.', 'ⅡⅢⅣ'.isdecimal())

# 判断字符串是否全部由数字组成
print('12.', '123'.isnumeric())
print('13.', '123四'.isnumeric())  # T
print('14.', 'ⅡⅢⅣ'.isnumeric())  # T

# 判断字符串是否全部由字母和数字组成
print('15.', 'abc1'.isalnum())
print('16.', '张三123'.isalnum())  # T
print('17.', 'abc!'.isalnum())  # F
