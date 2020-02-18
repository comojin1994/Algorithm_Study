def d(n):
    return n + sum(list(map(int, str(n))))


s1 = set()
s2 = set()

for i in range(10000):
    s1.add(d(i))
    s2.add(i)

L = list(s2 - s1)
L.sort()

for i in L:
    print(i)