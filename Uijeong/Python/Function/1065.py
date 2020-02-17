def d(k):
    L = list(map(int, str(k)))
    if len(L) == 1:
        return True
    d1 = L[1] - L[0]
    for i in range(len(L) - 1):
        d2 = L[i+1] - L[i]
        if d1 != d2:
            return False
        else:
            d1 = d2
    return True


n = int(input())
count = 0
for j in range(1, n + 1):
    if d(j):
        count += 1

print(count)
