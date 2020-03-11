import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    val = list(map(int, input().strip().split()))
    result = 0
    idx = 0
    while idx != N - 1:
        cnt = 0
        for i in range(idx + 1, N):
            if val[idx] > val[i]: cnt += 1
            else: break
        result = max(result, cnt)
        idx = i
    print(result)