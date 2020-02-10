import sys
input = sys.stdin.readline

N = int(input())

fac = {0:1, 1:1, 2:2, 3:6}

def facto(n):
    if n in fac.keys():
        return fac[n]
    result = n * facto(n-1)
    fac[n] = result
    return result

check = str(facto(N))
cnt = 0

for i in range(len(check)-1, -1, -1):
    if check[i] == '0':
        cnt += 1
    else:
        break
print(cnt)
