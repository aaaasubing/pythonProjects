# Editor: aaaasubing
# DevelopmentTime: 2021/4/21 11:26

# 为什么用列表
a = 10  # 变量存储的是一个对象的引用
# 列表存储的是多个对象的引用，每个对象有自己单独的id，type，value
lst = ['hello', 'world', 98]
print(id(lst))
print(type(lst))
print(lst)

# 列表的创建
# 创建列表的第一种方式：[]
lst1 = ['hello', 'world', 98]
print(lst1)
print(lst1[0], lst1[-4])  # -4为重复数据
# 创建列表的第二种方式：使用内置函数list()
lst2 = list(['hello', 'world', 98])

'''
列表的特点：
1.列表元素按照顺序有序排序
2.索引映射唯一一个数据
3.列表可以存储重复数据
4.任意数据类型混存
5.根据需要动态分配和回收内存
'''
