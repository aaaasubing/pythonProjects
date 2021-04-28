# Editor: aaaasubing
# DevelopmentTime: 2021/4/21 18:35
lst = [20, 40, 10, 98, 54]
print('排序前的列表', lst, id(lst))
# 开始排序，调用列表对象的sort方法，升序排序
lst.sort()
print('排序后的列表', lst, id(lst))  # 标识未更改，在原列表上进行的排序

# 通过指定关键字参数，将列表中的元素进行降序排序
# reverse=True 表示降序排序
lst.sort(reverse=True)
print(lst)
# reverse=False 表示降序排序
lst.sort(reverse=False)
print(lst)

# 使用内置函数sorted()对列表进行排序，将产生一个新的列表对象，原列表不发生改变
lst = [20, 40, 10, 98, 54]
print('排序前的列表', lst)
# 开始排序
new_lst = sorted(lst)  # 产生新的列表对象
print(new_lst)
# 指定关键字参数，实现列表元素降序排序
desc_lst = sorted(lst, reverse=True)
print(desc_lst)
