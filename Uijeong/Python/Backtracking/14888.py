import sys
import math

input = sys.stdin.readline


def dfs(x):
    if x == bp:
        ans = L[0]
        for i, o in enumerate(operator):
            if o == 0: ans += L[i+1]
            elif o == 1: ans -= L[i+1]
            elif o == 2: ans *= L[i+1]
            elif o == 3: ans = int(ans / L[i+1])
        ansL.append(ans)
        return
    for i in range(4):
        if opNum[i] > 0:
            operator.append(i)
            opNum[i] -= 1
            dfs(x+1)
            operator.pop(-1)
            opNum[i] += 1


if __name__ == "__main__":
    n = int(input())
    L = list(map(int, input().split()))
    opNum = list(map(int, input().split()))
    bp, operator, ansL = sum(opNum), [], []
    dfs(0)
    print(max(ansL))
    print(min(ansL))