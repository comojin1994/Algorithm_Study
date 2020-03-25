import sys
input = sys.stdin.readline


def LIS():
    dpL, dpR = [0] * 1002, [0] * 1002
    for i in range(1, n + 1):
        dpR[A[i]] = max(max(dpL[:A[i]]) + 1, max(dpR[A[i] + 1:]) + 1, dpR[A[i]])
        dpL[A[i]] = max(dpL[:A[i]]) + 1
    return max(max(dpL), max(dpR))


if __name__ == "__main__":
    n = int(input())
    A = [0] + list(map(int, input().split()))
    print(LIS())

'''
9
5 1 6 2 7 3 7 2 1
ans: 6

7
5 1 6 2 6 2 1
ans: 5

10
1 5 2 1 4 3 4 5 2 1
ans: 7

5
5 4 3 2 3
ans: 4

5
1 3 1 2 1
ans: 4
'''