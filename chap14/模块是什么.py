# Editor: aaaasubing
# DevelopmentTime: 2021/4/29 8:42
# 模块中有什么：函数、类（类属性、类方法，静态方法，实例方法）、语句
# 可以有n个模块，模块最终组成python程序
# 每个模块可以给不同的人开发，有利于团队开发，可以实现代码复用，不同模块之间可以避免变量名的冲突
def fun():
    pass


def fun2():
    pass


class Student:
    native_place = '吉林'  # 类属性

    def __init__(self, name, age):
        self.age = age
        self.name = name

    def eat(self, name, age):
        self.age = age
        self.name = name

    @classmethod
    def cm(cls):
        pass

    @staticmethod
    def sm():
        pass


a = 10
b = 20
print(a + b)
