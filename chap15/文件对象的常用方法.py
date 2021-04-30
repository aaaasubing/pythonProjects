# Editor: aaaasubing
# DevelopmentTime: 2021/4/30 9:29
file = open('a.txt', 'r')
print(file.read())  # 读取全部内容
print(file.read(2))  # 读取两个字符

print(file.readline())  # 读取一行
print(file.readlines())  # 每一行作为独立的字符串对象，最后放入列表返回

file.seek(2)  # 改变指针，到两个字节后，也就是一个字
print(file.read())
print(file.tell())  # 返回文件指针的当前位置
file.close()

file1 = open('c.txt', 'a')
lst = ['java', 'go', 'python']
file1.write('中国')  # 将字符串内容写入文件
file1.writelines(lst)  # 将列表内容写入文件
file1.close()

# flush()把缓冲区的内容写入文件，但不关闭文件
# close()把缓冲区的内容写入文件，关闭文件，释放文件对象相关资源
file2 = open('c.txt', 'a')
file2.write('hello')
file2.flush()
file2.write('world')
file2.close()  # flush之后还可以写，close之后不可以写，两者换位置以后，不能写入world
