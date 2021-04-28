# Editor: aaaasubing
# DevelopmentTime: 2021/4/12 15:37
# 转义字符
print('hello\nworld') # \+转义功能的首字符   n--newline
print('hello\tworld') # \t用了三个位置
print('helloooo\tworld') # \t用了四个位置
print('hello\rworld') # return  回车 只剩下world将hello进行了覆盖
print('hello\bworld') # back 退格 少一个o

print('http:\\\\www.baidu.com')  # \\打印出来是一个\
print('老师说：\‘大家好\’') # \是转义字符

# 原字符，不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上r或R
# 注意最后一个字符不能是反斜线\，可以是两个\\
print(r'hello\n world')
