# Editor: aaaasubing
# DevelopmentTime: 2021/4/23 18:32
"""
为什么要将元组设计成不可变序列：
在多任务环境下，同时操作对象时不需要加锁，因此在程序中尽量使用不可变序列
"""
"""
注意：元组中存储的是对象的引用
1.如果元组中的对象本身不可变对象，则不能再引用其他对象
2.如果元组中的对象是可变对象，则可变对象的引用不允许改变，但数据可以改变
"""
t = (10, [20, 30], 9)
print(t)
print(type(t))
print(t[0], type(t[0]), id(t[0]))
print(t[1], type(t[1]), id(t[1]))
print(t[2], type(t[2]), id(t[2]))
# 尝试将t[1]修改为100
print(id(100))
# t[1] = 100  # TypeError: 'tuple' object does not support item assignment
# 由于[20,30]是列表，列表是可变序列，所以可以将列表中添加元素，而列表的内存地址不变
t[1].append(100)
print(t, id(t[1]))


