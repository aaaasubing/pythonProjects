# Editor: aaaasubing
# DevelopmentTime: 2021/5/11 9:22
with open('logo.png', 'rb') as src_file:
    with open('copy2_logo.png') as target_file:
        target_file.write(src_file.read())

