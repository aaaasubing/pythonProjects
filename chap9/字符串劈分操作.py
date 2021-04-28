# Editor: aaaasubing
# DevelopmentTime: 2021/4/25 10:21
# 字符串的劈分操作，分割操作
s = 'hello world Python'
lst = s.split()  # 默认分隔符是空格，返回为列表类型
print(lst)

# 通过参数sep指定分隔符
s1 = 'hello|world|Python'
print(s1.split(sep='|'))

# 通过参数maxsplit指定分隔符的最大分割次数，经过最大分割次数后，其余的子串单独作为一部分
print(s1.split(sep='|', maxsplit=1))

# 从右侧开始劈分rsplit
print(s.rsplit())
print(s1.rsplit(sep='|'))
print(s1.rsplit(sep='|', maxsplit=1))  # 指定了最大分割次数后，左右分割就不一样了



