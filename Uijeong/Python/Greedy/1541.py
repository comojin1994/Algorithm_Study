import sys
input = sys.stdin.readline

if __name__ == "__main__":
    s = input().strip()
    L = [sum(list(map(int, li.split('+')))) for li in s.split('-')]
    print(L[0] - sum(L[1:]))