# Editor: aaaasubing
# DevelopmentTime: 2021/4/13 23:11
name = '玛利亚'
print(name)

# 变量有标识id(obj)，类型type(obj)，值value打印print(obj)
print('标识', id(name))
print('类型', type(name))
print('值', name)

# 变量的多次赋值，name指向新的空间，原来的地方没有东西了，被称为内存垃圾，垃圾回收机制进行回收
name = '玛利亚'
print(name)
name = '出溜冰'
print(name)

