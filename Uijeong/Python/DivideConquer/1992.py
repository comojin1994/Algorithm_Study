import sys

input = sys.stdin.readline


def DC(Map, k):
    ground = Map[0][0]
    flag = False
    for i in range(k):
        for j in range(k):
            if ground != Map[i][j]:
                flag = True
                break
    if flag:
        print("(", end='')
        DC([Map[i][:k // 2] for i in range(k // 2)], k // 2)
        DC([Map[i][k // 2:] for i in range(k // 2)], k // 2)
        DC([Map[i][:k // 2] for i in range(k // 2, k)], k // 2)
        DC([Map[i][k // 2:] for i in range(k // 2, k)], k // 2)
        print(")", end='')
    else:
        print(ground, end='')


if __name__ == "__main__":
    n = int(input())
    Map = [list(map(int, list(input().strip()))) for _ in range(n)]
    DC(Map, n)