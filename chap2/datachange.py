# Editor: aaaasubing
# DevelopmentTime: 2021/4/15 18:08
name = '张三'
age = 20

print(type(name), type(age))  # 说明name与age的数据类型不同
# print('我叫' + name + '，今年' + age + '岁')  # +为连接符，将不同类型的数据连接的时候会报错，解决方法：类型转换
print('我叫' + name + '，今年' + str(age) + '岁')  # 将int类型通过str()函数转成了str类型

print('------------str()将其他类型转成str类型------------')
a = 10
b = 198.8
c = False
print(type(a), type(b), type(c))
print(str(a), str(b), str(c), type(str(a)), type(str(b)), type(str(c)))

print('------------int()将其他类型转成int类型------------')
s1 = '128'
f1 = 98.7
s2 = "76.77"
ff = True
s3 = 'hello'
print(type(s1), type(f1), type(s2), type(ff), type(s3))
print(int(s1), type(int(s1)))  # 将str转成int，前提是字符串为数字串
print(int(f1), type(int(f1)))  # float转成int，截取整数部分，舍弃小数部分
# print(int(s2), type(int(s2)))  # 将str转成int类型，报错，因为字符串为小数串
print(int(ff), type(int(ff)))  # 将bool类型转成对应的数字
# print((int(s3), type(int(s3))))  # str转为int，字符串必须为数字串，且必须为整数串

print('------------float()将其他类型转成float类型------------')
s4 = '128.98'
s5 = "76"
fff = True
s6 = 'hello'
i = 98
print(type(s4), type(s5), type(fff), type(s6), type(i))
print(float(s4), type(float(s4)))
print(float(s5), type(float(s5)))  # int转为float，后面加.0
print(float(fff), type(float(fff)))  # 后面加.0
# print(float(s6), type(float(s6)))  # 报错，str里面是字符串不能转为float
print(float(i), type(float(i)))  # int转为float，后面加.0
