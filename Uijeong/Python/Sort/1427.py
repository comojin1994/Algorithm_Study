import sys

input = sys.stdin.readline

if __name__ == "__main__":
    L = list(map(int, input().strip()))
    L.sort(reverse=True)
    for li in L:
        print(li, end="")