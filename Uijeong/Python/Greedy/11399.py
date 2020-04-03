import sys
input = sys.stdin.readline


def ATM(q):
    q.sort()
    sum = 0
    for i, qi in enumerate(q):
        sum += (n-i) * qi
    return sum


if __name__ == "__main__":
    n = int(input())
    q = list(map(int, input().split()))
    print(ATM(q))