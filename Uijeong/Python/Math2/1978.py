import sys
import math

input = sys.stdin.readline


def isPrime(number):
    # 소수는 소인수가 1과 자기자신을 갖는 1보다 큰 자연수
    # 합성수는 제곱근보다 작은 소인수를 갖는다.
    if number == 1: return False

    m = math.floor(math.sqrt(number))

    for i in range(2, m + 1):
        if number % i == 0:
            return False
    return True


if __name__ == "__main__":
    n = int(input())
    L = list(map(int, input().split()))
    cnt = 0
    for li in L:
        if isPrime(li):
            cnt += 1
    print(cnt)