import sys
input = sys.stdin.readline

def func(K, L):
    cnt = 0
    while K != L:
        K, L = K // 2, L // 2
        cnt += 1
    print(cnt)
    return 1

if __name__ == '__main__':
    N, K, L = map(int, input().strip().split())
    func(K-1, L-1)