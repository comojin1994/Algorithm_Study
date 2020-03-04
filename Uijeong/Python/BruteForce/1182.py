import sys
from itertools import combinations

input = sys.stdin.readline


if __name__ == "__main__":
    N, S = map(int, input().split())
    L = list(map(int, input().split()))

    cnt = 0
    for i in range(1, N+1):
        combi = combinations(L, i)
        for cb in combi:
            if S == sum(list(cb)):
                cnt += 1
    print(cnt)