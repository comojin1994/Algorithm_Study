import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    A = sorted(list(map(int, input().strip().split())))
    B = sorted(list(map(int, input().strip().split())), reverse=True)
    sum = 0
    for a, b in zip(A, B):
        sum += a*b
    print(sum)