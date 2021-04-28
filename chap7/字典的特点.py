# Editor: aaaasubing
# DevelopmentTime: 2021/4/23 8:16
d = {'name': '张三', 'name': '李四'}  # key不允许重复
print(d)

dd = {'name': '张三', 'nikename': '张三'}  # value可以重复
print(dd)

# 元素是无序的
lst = [10, 20, 30]
lst.insert(1, 100)
print(lst)

# 元素内对象是不可变对象，例如列表不可以
# d = {lst: 100}  # TypeError: unhashable type: 'list'

# 可根据需要动态伸缩
# 会浪费较大内存，使用空间换时间
