import sys
import math
input = sys.stdin.readline

T = int(input())

def get_prime_list(n):
    li = [True for _ in range(n + 1)]
    li[0], li[1] = False, False

    for i in range(2, int(math.sqrt(n + 1)) + 1):
        if li[i] == False:
            continue
        for j in range(i * 2, n + 1, i):
            li[j] = False

    prime = []
    for idx, b in enumerate(li):
        if b == True:
            prime.append(idx)
    return prime

for _ in range(T):
    N = int(input())
    prime = get_prime_list(N)
    idx_li= [prime[i] for i, _ in enumerate(prime) if prime[i] <= N//2]
    il = len(idx_li)

    for i in range(il-1, -1, -1):
        if N - idx_li[i] in prime:
            print(idx_li[i], N - idx_li[i])
            break