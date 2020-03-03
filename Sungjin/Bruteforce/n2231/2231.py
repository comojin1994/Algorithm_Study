import sys
input = sys.stdin.readline

N = list(input().strip())
a = int(N[0])
leng = len(N)-1
N = int(''.join(N))
value = True

for n in range((a-1)*(10**leng), (a+1)*(10**leng)):
    value = n + sum([int(m) for m in list(str(n))])
    if value == N:
        value = False
        print(n)
        break

if value:
    print(0)