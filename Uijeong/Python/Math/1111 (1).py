import sys
import math

input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    L = list(map(int, input().split()))

    if N == 1:
        print("A")
    elif N == 2:
        if L[0] == L[1]:
            print(L[0])
        else:
            print("A")
    else:
        a = 0
        if L[1] - L[0] != 0:
            a = (L[2] - L[1]) // (L[1] - L[0])
        b = L[1] - L[0] * a
        for i in range(N-1):
            if L[i+1] != L[i] * a + b:
                print("B")
                exit(0)

        print(L[N-1] * a + b)




