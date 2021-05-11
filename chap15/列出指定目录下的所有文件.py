# Editor: aaaasubing
# DevelopmentTime: 2021/5/11 9:58
import os
path = os.getcwd()
lst = os.listdir(path)
for filename in lst:
    if filename.endswith('.py'):
        print(filename)

