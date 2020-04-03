import sys
import math
input = sys.stdin.readline


def greedy():
    global k
    cnt = 0
    for i in range(n-1, -1, -1):
        num = k / A[i]
        if num < 1:
            continue
        else:
            num = math.floor(num)
            k = k - num * A[i]
            cnt += num
            if k == 0: break
    return cnt


if __name__ == "__main__":
    n, k = map(int, input().split())
    A = [int(input()) for _ in range(n)]
    print(greedy())