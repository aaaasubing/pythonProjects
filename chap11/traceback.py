# Editor: aaaasubing
# DevelopmentTime: 2021/4/27 10:43
# print(10/0)
import traceback

try:
    print('-------------')
    print(1 / 0)
except:
    traceback.print_exc()
