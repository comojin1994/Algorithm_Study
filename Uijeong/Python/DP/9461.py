import sys

input = sys.stdin.readline


def seq(n):
    P = [0, 1, 1, 1, 2, 2]
    if n > 4:
        P += [0] * (n-5)
        for i in range(6, n+1):
            P[i] = P[i-1] + P[i-5]
    return P[n]


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(seq(n))