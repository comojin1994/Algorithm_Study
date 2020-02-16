import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    L = list(map(int, input().split()))
    minL = min(L)
    maxL = max(L)

    print(minL, maxL)
