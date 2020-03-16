import sys
input = sys.stdin.readline


def rgb():
    [r, g, b] = RGB[0]
    for i in range(1, n):
        [ri, gi, bi] = RGB[i]
        tmp = [min(g, b) + ri, min(r, b) + gi, min(r, g) + bi]
        r, g, b = tmp[0], tmp[1], tmp[2]
    return min(r, g, b)


if __name__ == "__main__":
    n = int(input())
    RGB = [list(map(int, input().split())) for _ in range(n)]
    print(rgb())