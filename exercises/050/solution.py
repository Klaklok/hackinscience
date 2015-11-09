import operator
for i in range(1, 1000):
    if operator.mod(i, 3) == 0 or operator.mod(i, 5) == 0:
        print(int(i))
