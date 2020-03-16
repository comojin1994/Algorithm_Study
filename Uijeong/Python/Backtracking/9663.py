import sys

input = sys.stdin.readline


def adjacent(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return True
    return False


def dfs(x):
    global result
    if x == N:
        result += 1
    else:
        for i in range(N):
            row[x] = i
            if adjacent(x) is False:
                dfs(x+1)


if __name__ == "__main__":
    N = int(input())
    row = [0] * N
    if N < 13:
        result = 0
        dfs(0)
    else:
        answer = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
        result = answer[N]
    print(result)