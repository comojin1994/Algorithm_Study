L = []
for i in range(9):
    L.append(int(input()))

maxL = max(L)
print(maxL)
print(L.index(maxL) + 1)