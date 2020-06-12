import sys, math
input = sys.stdin.readline

if __name__ == '__main__':
    for _ in range(int(input())):
        N, M = map(int, input().strip().split())
        print(math.factorial(M) // (math.factorial(N) * math.factorial(M-N)))