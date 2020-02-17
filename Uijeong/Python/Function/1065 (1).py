def d(a):
    x = a % 10
    y = a // 10 % 10
    z = a // 100 % 10
    if x + y == 2 * y:
        return True
    else:
        return False


n = int(input())
count = 0
for i in range(1, n+1):
    count += d(i)
    print(count)
