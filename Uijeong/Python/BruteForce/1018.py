import sys

input = sys.stdin.readline


def chess(x, y):
    cntW, cntB = 0, 0
    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                if j % 2 == 0:
                    # B 로 시작
                    if L[y + i][x + j] != "B":
                        cntB += 1
                    elif L[y + i][x + j] != "W":
                        cntW += 1
                else:
                    if L[y + i][x + j] != "W":
                        cntB += 1
                    elif L[y + i][x + j] != "B":
                        cntW += 1
            else:
                if j % 2 == 0:
                    if L[y + i][x + j] != "W":
                        cntB += 1
                    elif L[y + i][x + j] != "B":
                        cntW += 1
                else:
                    if L[y + i][x + j] != "B":
                        cntB += 1
                    elif L[y + i][x + j] != "W":
                        cntW += 1

    return cntW if cntW < cntB else cntB


if __name__ == "__main__":
    n, m = map(int, input().split())
    L, Li = [], []

    for _ in range(n):
        line = input()
        L.append(line)

    Li = [chess(x, y) for x in range(m-7) for y in range(n-7)]
    print(min(Li))