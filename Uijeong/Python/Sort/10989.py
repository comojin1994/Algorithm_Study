import sys

input = sys.stdin.readline


def count_sort():
    k = max(L) + 1
    C = [0] * k

    # count
    i, lenL = 0, len(L)
    for j in range(lenL):
        C[L[j]] = C[L[j]] + 1

    # rearrange
    for j in range(k):
        while C[j] > 0:
            L[i] = j
            C[j] = C[j] - 1
            i += 1
    return L


if __name__ == "__main__":
    n = int(input())

    L = count_sort()
    for li in L:
        print(li)