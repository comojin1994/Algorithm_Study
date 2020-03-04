import sys
import math

input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    x = int(n ** 0.5)
    N = n-1
    i = n
    cnt = 0
    while i != 0:
        cnt += (N//i+1) * (i - N//(N//i+1))
        i = N//(N//i+1)
    print(cnt)