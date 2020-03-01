n = int(input())

L = []
for _ in range(n):
    L.append(int(input()))

L.sort()
for li in L:
    print(li)