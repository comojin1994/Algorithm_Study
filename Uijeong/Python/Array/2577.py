a = int(input())
b = int(input())
c = int(input())

mul = a * b * c
L = list(map(int, str(mul)))
for i in range(10):
    print(L.count(i))
