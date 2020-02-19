import sys

input = sys.stdin.readline

a, b = map(int, input().split())

flag = 'a'
for i in range(3):
    tmpA = a // (10 ** i) % 10
    tmpB = b // (10 ** i) % 10

    if tmpA > tmpB:
        flag = 'a'
        break
    elif tmpA < tmpB:
        flag = 'b'
        break
    else:
        flag = 'eq'
        continue
p = 0
if flag == 'a':
    for i in range(3):
        p += a // (10 ** i) % 10 * (10 ** (2 - i))
else:
    for i in range(3):
        p += b // (10 ** i) % 10 * (10 ** (2 - i))

print(p)