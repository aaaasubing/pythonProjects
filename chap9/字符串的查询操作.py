# Editor: aaaasubing
# DevelopmentTime: 2021/4/24 19:18
# 字符串的查询操作
s = 'hello,hello'
print(s.index('lo'))
print(s.find('lo'))
print(s.rindex('lo'))
print(s.rfind('lo'))

# print(s.index('k'))  # ValueError: substring not found
print(s.find('k'))  # -1  不抛出异常
# print(s.rindex('k'))  # ValueError: substring not found
print(s.rfind('k'))  # -1  不抛出异常



