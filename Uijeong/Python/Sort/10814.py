import sys

input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    L = [input().strip().split() for _ in range(n)]
    L = sorted(L, key=lambda x: int(x[0]))
    for [age, name] in L:
        print(age, name)
