import sys

input = sys.stdin.readline


def tile(x):
    for i in range(3, x+1):
        T[i] = (T[i-2] % 15746 + T[i-1] % 15746) % 15746
    return T[x]


if __name__ == "__main__":
    n = int(input())
    T = [0, 1, 2] + [0] * (n-1)
    print(tile(n))