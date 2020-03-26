import sys
import copy
input = sys.stdin.readline


def stair():
    Fi_2, Fi_1, cnt = [0], [0, score[0]], 1
    for i in range(1, n):
        tmp = max(Fi_1)
        cnt += 1
        if cnt == 3:
            cnt -= 1
            tmp = Fi_1[0]

        maxFi_2 = max(Fi_2)
        Fi_2 = copy.deepcopy(Fi_1)
        Fi_1 = [maxFi_2 + score[i], tmp + score[i]]
    return max(Fi_1)


if __name__ == "__main__":
    n = int(input())
    score = [int(input()) for _ in range(n)]
    print(stair())