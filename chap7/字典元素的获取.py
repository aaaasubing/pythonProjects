# Editor: aaaasubing
# DevelopmentTime: 2021/4/22 9:21
# 获取字典中的元素
scores = {'张三': 100, '李四': 98, '王五': 45}

# 1.使用[]
print(scores['张三'])
# print(scores['陈六'])  # KeyError: '陈六'  报错

# 2.使用get()方法
print(scores.get('张三'))
print(scores.get('陈六'))  # None，不报错
print(scores.get('麻七', 99))  # 99是查找指定的键不存在的时候给的默认值
