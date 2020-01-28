import sys
import math
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break

    li = [True for _ in range(2*n+1)]
    li[0] = False
    li[1] = False

    for i in range(2, int(math.sqrt(2*n))+1):
        if li[i] == False:
            continue
        for j in range(i*2, 2*n+1, i):
            li[j] = False

    cnt = 0
    for i in li[n+1:]:
        if i == True:
            cnt = cnt + 1
    print(cnt)