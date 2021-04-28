# Editor: aaaasubing
# DevelopmentTime: 2021/4/22 11:20
# key的判断
scores = {'张三': 100, '李四': 98, '王五': 45}
print('张三' in scores)
print('张三' not in scores)
# 删除指定的key-value对
del scores['张三']
# scores.clear()  # 清空字典的所有元素
print(scores)
# 字典元素的新增
scores['陈六'] = 98
print(scores)
# 字典元素的修改
scores['陈六'] = 100
print(scores)
