import sys
input = sys.stdin.readline


def Big():
    Li = []
    for i in L:
        cnt = 1
        for j in L:
            if i[0] < j[0] and i[1] < j[1]:
                cnt += 1
        Li.append(cnt)
    return Li


if __name__ == "__main__":
    n = int(input())
    L = []
    for _ in range(n):
        x, y = map(int, input().split())
        L.append((x, y))

    for rank in Big():
        print(rank, end=" ")