import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


# # top-down 시간초과
# def make_top_down(x):
#     global L
#     if L[x] > 0: # break point
#         return L[x]
#     if x % 3 == x % 2 == 0:
#         L[x] = min(make(x // 3) + 1, make(x // 2) + 1, make(x - 1) + 1)
#     elif x % 3 == 0:
#         L[x] = min(make(x//3) + 1, make(x-1) + 1)
#     elif x % 2 == 0:
#         L[x] = min(make(x//2) + 1, make(x-1) + 1)
#     else:
#         L[x] = make(x-1) + 1
#     return L[x]


def make(x):
    for i in range(4, x + 1):
        if i % 3 == 0 and i % 2 == 0:
            L[i] = min(L[i // 3] + 1, L[i // 2] + 1, L[i - 1] + 1)
        elif i % 3 == 0:
            L[i] = min(L[i // 3] + 1, L[i - 1] + 1)
        elif i % 2 == 0:
            L[i] = min(L[i // 2] + 1, L[i - 1] + 1)
        else:
            L[i] = L[i - 1] + 1
    return L[x]


if __name__ == "__main__":
    x = int(input())
    L = [0, 0, 1, 1] + [0] * (x-3)
    print(make(x))