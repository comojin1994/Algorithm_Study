import sys

input = sys.stdin.readline


def jack():
    L = []
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                L.append(cards[i] + cards[j] + cards[k])
    L = filter(lambda x: x <= m, L)
    return max(L)


if __name__ == "__main__":
    n, m = map(int, input().split())
    cards = list(map(int, input().split()))
    print(jack())
