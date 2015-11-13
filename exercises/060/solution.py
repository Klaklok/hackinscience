alpha = ("abcdefghijklmnopqrstuvwxyz")
n = int(0)
while n < 26:
    for i in range(0, 26, 1):
        print(alpha[i]+alpha[n])
    n += 1
