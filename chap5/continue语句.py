# Editor: aaaasubing
# DevelopmentTime: 2021/4/20 20:26
# continue: 结束当前循环，进入下一循环
# 要求：输出1到50之间所有5的倍数（和5的余数为0）
for item in range(1, 51):
    if item % 5 == 0:
        print(item)

# 使用continue
for item in range(1, 51):
    if item % 5 != 0:
        continue
    else:
        print(item)
