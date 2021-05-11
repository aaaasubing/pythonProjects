# Editor: aaaasubing
# DevelopmentTime: 2021/5/11 10:03
import os
path = os.getcwd()
lst_files = os.walk(path)
for dirpath, dirname, filename in lst_files:
    """print(dirpath)
    print(dirname)
    print(filename)
    print('-----------')"""
    for dir in dirname:
        print(os.path.join(dirpath, dir))
    for file in filename:
        print(os.path.join(dirpath, file))
    print('-------------------')