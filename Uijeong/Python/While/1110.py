import sys

input = sys.stdin.readline

n = input().strip()
n = "0" + n if int(n) < 10 else n
z = n

count = 0
while True:
    count += 1

    x, y = map(int, [z[0], z[1]])
    z = str(x + y)
    z = str(y) + z[-1]

    if z == n:
        break

print(count)
