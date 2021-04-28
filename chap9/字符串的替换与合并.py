# Editor: aaaasubing
# DevelopmentTime: 2021/4/25 10:39
# 字符串的替换replace，第一个参数指定被替换的子串，第二个参数指定替换子串的字符串，该方法返回替换后得到的字符串，替换前字符串不发生变化，第三个参数指定最大替换次数
s = 'hello,Python'
print(s.replace('Python', 'Java'))
s1 = 'hello,Python,Python,Python'
print(s1.replace('Python', 'Java', 2))

# 字符串的合并，将列表或元组中的字符串合并成一个字符串
lst = ['hello', 'Java', 'Python']
print('|'.join(lst))
print(''.join(lst))

t = ('hello', 'Java', 'Python')
print(''.join(t))

print('*'.join('Python'))  # P*y*t*h*o*n 将Python作为字符串序列去进行连接

