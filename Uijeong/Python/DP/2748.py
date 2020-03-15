import sys

input = sys.stdin.readline


def fibonacci_bottom_up(n):
    F = [0, 1]
    for i in range(2, n+1):
        F.append(F[i-2] + F[i-1])
    return F[n]


def fibonacci_top_down(x):
    if F_t[x] >= 0:
        return F_t[x]
    F_t[x] = fibonacci_top_down(x-1) + fibonacci_top_down(x-2)
    return F_t[x]


if __name__ == "__main__":
    n = int(input())
    F_t = [0, 1] + [-1] * (n-1)
    # print(fibonacci_bottom_up(n))
    print(fibonacci_top_down(n))