# Editor: aaaasubing
# DevelopmentTime: 2021/4/27 8:50
def fac(n):
    if n == 1:
        return
    else:
        res = n * fac(n-1)
        return res


print(fac(6))
