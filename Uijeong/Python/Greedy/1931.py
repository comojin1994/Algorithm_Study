import sys
input = sys.stdin.readline


def ASP(L):
    L = sorted(L, key=lambda x: [x[1], x[0]])
    cnt, i = 1, 1
    conf = L[0]
    while i < n:
        if L[i][0] >= conf[1]:
            cnt += 1
            conf = L[i]
        i += 1
    return cnt


if __name__ == "__main__":
    n = int(input())
    L = [list(map(int, input().split())) for _ in range(n)]
    print(ASP(L))
