import sys

input = sys.stdin.readline

if __name__ == "__main__":
    a, b = map(int, input().split())
    L = []
    for i in range(1, 1001):
        L += [i] * i
    L = L[a-1:b]
    print(sum(L))