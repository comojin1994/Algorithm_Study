import sys
import math

input = sys.stdin.readline


if __name__ == "__main__":
    N, A, B = map(int, input().split())
    d = int(math.log(N, 2))
    for di in range(d, -1, -1):
        grA = math.ceil(A/(2**di))
        grB = math.ceil(B/(2**di))
        if grA != grB:
            print(di+1)
            break
