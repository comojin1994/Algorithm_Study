import sys
input = sys.stdin.readline

N = int(input())

shape = {3: [['*', '*', '*'], ['*', ' ', '*'], ['*', '*', '*']]}

def draw(N):
    if N in shape:
        return shape[N]
    li = [[0]*N for _ in range(N)]
    k = N//3
    for i in range(N):
        for j in range(N):
            if i >= k and i < k*2 and j >= k and j < k*2:
                li[i][j] = ' '
            else:
                li[i][j] = draw(k)[i%k][j%k]
    shape[N] = li
    return shape[N]

draw(N)
for i in range(N):
    for j in range(N):
        print(shape[N][i][j], end='')
    print()