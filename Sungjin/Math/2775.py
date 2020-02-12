import sys
input = sys.stdin.readline

building = [[0]*14 for _ in range(15)]

def cal_per(k, n):
    if k == 0:
        return n
    else:
        sum = 0
        for i in range(n):
            sum = sum + building[k-1][i]
        return sum

def cal_build(building, k, n):
    for i in range(k+1):
        for j in range(1, n+1):
            building[i][j-1] = cal_per(i, j)
    return building

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    building = cal_build(building, k, n)
    print(building[k][n-1])
