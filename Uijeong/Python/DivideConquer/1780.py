import sys
input = sys.stdin.readline


def divide(paper, k):
    global s, m, e
    ground = paper[0][0]
    for row in paper:
        for x in row:
            if x != ground:
                for i in range(3):
                    temp = paper[k // 3 * i:k // 3 * (i + 1)]
                    for j in range(3):
                        divide([li[k // 3 * j:k // 3 * (j + 1)] for li in temp], k // 3)
                return
    if ground == -1:
        s += 1
    elif ground == 0:
        m += 1
    else:
        e += 1


if __name__ == "__main__":
    n = int(input())
    paper = [list(map(int, input().split())) for _ in range(n)]
    s, m, e = 0, 0, 0
    divide(paper, n)
    print('\n'.join(map(str, [s, m, e])))
