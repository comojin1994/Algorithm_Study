import sys

input = sys.stdin.readline


if __name__ == "__main__":
    N, M = map(int, input().split())
    L = [list(input().strip()) for _ in range(M)]
   sc = 0
   for i in range(M):
       for j in range(N):
           if j == 0:
               if L[i][j] == "W":
                   sc += 1
               else:
                   sc = 0

            



