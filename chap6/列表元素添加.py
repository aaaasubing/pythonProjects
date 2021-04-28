# Editor: aaaasubing
# DevelopmentTime: 2021/4/21 18:11

# 向列表末尾添加一个元素，标识相同，同一个列表对象
lst = [10, 20, 30]
lst.append(100)
print(lst)

# 列表末尾至少添加一个元素
lst2 = ['hello', 'world']
# lst.append(lst2)   # lst2作为一个元素放入lst末尾
lst.extend(lst2)  # 添加lst2每个元素分别添加到lst末尾
print(lst)

# 列表的任意位置添加一个元素
lst.insert(1, 90)
print(lst)

# 列表的任意位置添加至少一个元素（切片，切掉的位置用新的list代替）
lst3 = [True, False, 'hello']
lst[1:] = lst3
print(lst)
