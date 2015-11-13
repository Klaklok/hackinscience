alpha = "abcdefghijklmnopqrstuvwxyz"
for i in range(0, 26):
    for j in range(i, 26):
        if i != j:
            print(alpha[i]+alpha[j])
