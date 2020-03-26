import sys
import copy
input = sys.stdin.readline


def easy_stair(Li_1):
    Li = [0] * 10
    for i in range(1, n):
        for j in range(10):
            if j == 0:
                Li[j + 1] = (Li[j + 1] + Li_1[j]) % 1000000000
            elif j == 9:
                Li[j - 1] = (Li[j - 1] + Li_1[j]) % 1000000000
            else:
                Li[j + 1] = (Li[j + 1] + Li_1[j] % 1000000000) % 1000000000
                Li[j - 1] = (Li[j - 1] + Li_1[j] % 1000000000) % 1000000000
        Li_1 = copy.deepcopy(Li)
        Li = [0] * 10
    Li_1 = list(map(lambda x: x % 1000000000, Li_1))
    return sum(Li_1) % 1000000000


if __name__ == "__main__":
    n = int(input())
    Li_1 = [0] + [1] * 9
    print(easy_stair(Li_1))