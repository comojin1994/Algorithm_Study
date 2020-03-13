import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, Q = map(int,input().strip().split())
    cow = list(map(int, input().strip().split()))
    Ou = list(map(int, input().strip().split()))
    result = [0 for _ in range(N)]
    result[0] = cow[0] * cow[1] * cow[2] * cow[3]
    for i in range(1, N):
        result[i] = (result[i-1] // cow[i-1]) * cow[(i+3) % N]
    S = sum(result)
    for o in Ou:
        for i in range(1, 5):
            S -= 2*result[o-i]
            result[o-i] *= -1
        print(S)