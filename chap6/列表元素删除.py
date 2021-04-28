# Editor: aaaasubing
# DevelopmentTime: 2021/4/21 18:20
lst = [10, 20, 30, 40, 50, 60, 30]
lst.remove(30)  # 从列表中溢出一个元素，如果有重复元素只移除第一个元素
print(lst)
# lst.remove(100)  # ValueError: list.remove(x): x not in list

# pop()根据索引移除元素
lst.pop(1)
print(lst)
# lst.pop(5)  # IndexError: pop index out of range 指定的索引位置不存在，抛出异常
lst.pop()  # 不写参数，默认删除最后一个元素
print(lst)

# 切片操作，删除至少一个元素，将产生一个新的列表对象
new_lst = lst[1:3]
print('原列表', lst)
print('切片后的列表', new_lst)

# 不产生新的列表对象，而是删除原列表中的内容（用空列表进行替代）
lst[1:3] = []
print(lst)

# clear()清空列表  元素
lst.clear()
print(lst)  # []

# del删除列表  对象
del lst
# print(lst)  # NameError: name 'lst' is not defined
