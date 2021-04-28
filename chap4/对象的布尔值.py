# Editor: aaaasubing
# DevelopmentTime: 2021/4/16 21:23
# 测试对象的布尔值
# 可以把对象直接放在if条件语句中判断，写下一步语句
print('---------以下对象的布尔值为False-----------')
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(''))  # 长度为0的字符串对象
print(bool(""))  # 长度为0的字符串对象
print(bool([]))  # 空列表[]
print(bool(list()))  # 空列表
print(bool(()))  # 空元组
print(bool(tuple()))  # 空元祖
print(bool({}))  # 空字典
print(bool(dict()))  # 空字典
print(bool(set()))  # 空集合

print('---------除以上，其他对象的布尔值为True-----------')
print(bool(18))
print(bool(True))
print(bool('helloworld'))  # 不是空字符串
