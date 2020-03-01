import sys

input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    L = list(set([input().strip() for _ in range(n)]))
    L = sorted(L, key=lambda x: [len(x), x])
    for li in L:
        print(li)