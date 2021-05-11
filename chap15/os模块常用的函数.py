# Editor: aaaasubing
# DevelopmentTime: 2021/5/11 9:25
# os模块是与操作系统相关的一个模块
import os
os.system('notepad.exe')
os.system('calc.exe')
# 直接调用可执行文件
os.startfile('C:\\Users\\surface\\Pictures\\壁纸\\img-f454d915f1d08876dead5f40a212f6ff.jpg.JPG')

# 返回当前的工作目录
print(os.getcwd())
# 返回指定路径下的文件和目录信息
lst = os.listdir('../chap15')
print(lst)
# 创建目录
os.mkdir('new_dir')
# 创建多级目录
os.mkdirs('A/B/C')
# 删除目录
os.rmdir('new_dir')
os.rmdirs('A/B/C')
# 将path设置为当前工作目录
os.chdir('D:\\Projects\\pythonProjects\\chap14')
print(os.getcwd())
