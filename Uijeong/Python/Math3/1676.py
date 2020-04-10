import sys
import math
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    cnt = 0
    for i in reversed(str(math.factorial(n))):
        if int(i) > 0: break
        cnt += 1
    print(cnt)