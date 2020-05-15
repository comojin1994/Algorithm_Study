import sys
input = sys.stdin.readline


def DC(Map, k):
    global white, black
    ground = Map[0][0]
    flag = True
    for i in range(k):
        for j in range(k):
            if ground != Map[i][j]:
                flag = False
                break
    if flag:
        if ground:
            black += 1
        else:
            white += 1
    else:
        DC([Map[i][:k // 2] for i in range(k // 2)], k // 2)
        DC([Map[i][k // 2:] for i in range(k // 2)], k // 2)
        DC([Map[i][:k // 2] for i in range(k // 2, k)], k // 2)
        DC([Map[i][k // 2:] for i in range(k // 2, k)], k // 2)


if __name__ == "__main__":
    n = int(input())
    Map = [list(map(int, input().split())) for _ in range(n)]
    white, black = 0, 0
    DC(Map, n)
    print(white)
    print(black)
