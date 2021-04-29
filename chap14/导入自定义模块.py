# Editor: aaaasubing
# DevelopmentTime: 2021/4/29 9:16
# 在该模块中导入calc自定义模块的使用
# 把整个文件夹作为source源
import calc
print(calc.add(10, 20))
print(calc.div(10, 4))

# 或者用：
'''
from calc import add
print(add(10, 20))
'''

# git
# git config --global http.sslVerify "false"