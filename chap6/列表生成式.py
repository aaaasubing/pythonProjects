# Editor: aaaasubing
# DevelopmentTime: 2021/4/21 18:44
# 使用列表生成式要求列表中的元素都有一定的规则
lst = [i for i in range(1, 10)]
print(lst)
lst1 = [i*i for i in range(1, 10)]
print(lst1)

# 要求：列表中的元素的值为2,4,6,8,10
lst2 = [i*2 for i in range(1, 6)]
print(lst2)
