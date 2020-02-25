import math


def minRoom(n):
    if n == 1: return 1

    k = math.ceil(math.sqrt((n - 1) / 3)) + 1
    for i in range(k, 0, -1):
        if 3*(i**2) - 3*i + 1 < n <= 3*(i**2) + 3*i + 1:
            return i + 1


if __name__ == "__main__":
    n = int(input())
    print(minRoom(n))