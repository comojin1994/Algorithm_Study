n = int(input())

total = 10000
for i in range(n//3 + 1):
    for j in range(n//5 + 1):
        kg = 3 * i + 5 * j

        if kg == n and i + j < total:
            total = i + j

if total == 10000:
    print(-1)
else:
    print(total)