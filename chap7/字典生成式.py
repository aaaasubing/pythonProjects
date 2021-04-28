# Editor: aaaasubing
# DevelopmentTime: 2021/4/23 8:39
items = ['Fruits', 'Books', 'Others']
prices = [96, 78, 85]
d = {items.upper(): prices for items, prices in zip(items, prices)}  # upper变成大写，zip使用短的那个字典进行生成
print(d)
