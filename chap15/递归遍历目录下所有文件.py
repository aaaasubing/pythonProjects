# Editor: aaaasubing
# DevelopmentTime: 2021/5/11 10:03
import os
path = os.getcwd()
lst_files = os.walk(path)
for dirpath, dirname, filename in lst_files:
    print(dirpath)
    print(dirname)
    print(filename)
    print('-----------')
