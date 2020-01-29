import sys
input = sys.stdin.readline

T = int(input())

li = [True for _ in range(10001)]
li[0], li[1] = False, False

for i in range(2, 98):
    if li[i] == False:
        continue
    for j in range(i * 2, 10001, i):
        li[j] = False

for _ in range(T):
    N = int(input())
    m = N // 2
    for i in range(m, 1, -1):
        if li[N-i] == True and li[i] == True:
            print(i, N-i)
            break