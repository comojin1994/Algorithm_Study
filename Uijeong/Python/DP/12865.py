import sys
input = sys.stdin.readline


def Knapsack():
    for i in range(1, n+1):
        for j in range(1, k+1):
            weight, value = stuff[i][0], stuff[i][1]
            if weight > j:
                knapsack[i][j] = knapsack[i-1][j]
            else:
                knapsack[i][j] = max(value + knapsack[i-1][j-weight], knapsack[i-1][j])
    return knapsack[n][k]


if __name__ == "__main__":
    n, k = map(int, input().split())
    knapsack = [[0] * (k+1) for _ in range(n+1)]
    stuff = [[0, 0]]
    for _ in range(n):
        stuff.append(list(map(int, input().split())))
    print(Knapsack())


