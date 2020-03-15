import sys
import math

input = sys.stdin.readline


if __name__ == "__main__":
    n, k = map(int, input().split())
    L = list(map(int, input().split()))
    idx = L.index(min(L))
    min = 1000000001
    for i in range(idx, idx-k+1, -1):
        tmp = math.ceil((n - i - 1) / (k - 1)) + math.ceil(i / (k - 1))
        if min >= tmp:
            min = tmp
    print(min)
