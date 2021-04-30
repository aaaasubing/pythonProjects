# Editor: aaaasubing
# DevelopmentTime: 2021/4/30 9:21
# r只读模式

# w为只写模式，不存在则创建，存在则覆盖原有内容
file = open('b.txt', 'w')
file.write('Python')  # 用write进行替换原有内容
file.close()

# a追加模式，不存在则创建，指针在文件开头，文件存在，在文件末尾追加内容，指针在文件末尾
file = open('b.txt', 'a')
file.write('Python')
file.close()

# b以二进制方式打开文件，不能单独使用，需要与其他模式一起使用，rb或者rw
src_file = open('logo.png', 'rb')
target_file = open('copy_logo.png', 'wb')
target_file.write(src_file.read())  # 边读边写
src_file.close()

# +以读写模式打开，不能单独使用，需要与其他模式一起使用，a+
