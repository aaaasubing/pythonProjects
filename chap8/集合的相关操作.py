# Editor: aaaasubing
# DevelopmentTime: 2021/4/24 10:39
s = {10, 20, 405, 60}
# 判断操作
print(10 in s)
print(100 in s)
print(10 not in s)
print(100 not in s)
# 新增操作
s.add(80)  # 一次一个
print(s)
s.update({200, 300, 400})  # 一次多个元素，至少一个，集合
print(s)
s.update([45, 46, 47])  # 列表
s.update((78, 90, 100))  # 元组
print(s)
# 删除操作
s.remove(100)
print(s)
# s.remove(500)  # KeyError: 500   不存在抛出异常
s.discard(500)  # 不存在不抛出异常
s.pop()  # 一次删除一个任意元素，不可以指定参数
print(s)
s.clear()  # 清空元素
print(s)

