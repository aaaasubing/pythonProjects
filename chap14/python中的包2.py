# Editor: aaaasubing
# DevelopmentTime: 2021/4/29 18:25
# 导入带有包的模块时的注意事项
# 使用import方式进行导入，只能写包名或者模块名
import pageage1
import calc

# from方式进行导入可以导入函数名，模块名，变量名
from pageage1 import module_A
from pageage1.module_A import a


