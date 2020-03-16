import sys

input = sys.stdin.readline


def fibonacci(x):
    if F[x] != [-1, -1]:
        return F[x]
    x_1, x_2 = fibonacci(x-1), fibonacci(x-2)
    F[x] = [x_2[0] + x_1[0], x_2[1] + x_1[1]]
    return F[x]


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        F = [[1, 0], [0, 1]] + [[-1, -1]] * (n-1)
        fi = fibonacci(n)
        print(fi[0], fi[1])