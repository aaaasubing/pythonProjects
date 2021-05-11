# Editor: aaaasubing
# DevelopmentTime: 2021/5/11 9:37
import os.path
# 获取文件或目录的绝对路径
print(os.path.abspath('with语句.py'))  # 文件的绝对路径
# 用于判断文件或目录是否存在，存在返回True，否则False
print(os.path.exists('with语句.py'), os.path.exists('demo11.py'))
# 将目录与目录或者文件名拼接起来
print(os.path.join('D:\\Projects\\pythonProjects', 'with语句.py'))
# 从一个目录中提取文件名
print(os.path.split('D:\\Projects\\pythonProjects\\chap15\\with语句.py'))
# 分离文件名和扩展名
print(os.path.splitext('with语句.py'))
# 从一个路径中提取文件名
print(os.path.basename('D:\\Projects\\pythonProjects\\chap15\\with语句.py'))
# 从一个路径中提取文件路径，不包括文件名
print(os.path.dirname('D:\\Projects\\pythonProjects\\chap15\\with语句.py'))
# 用于判断是否为路径
print(os.path.isdir('D:\\Projects\\pythonProjects\\chap15\\with语句.py'))  # False，最后的是文件
