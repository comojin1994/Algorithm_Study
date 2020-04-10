import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, A, B = map(int, input().strip().split())
    A_li = sorted(list(map(int, input().strip().split())), reverse=True)
    B_li = sorted(list(map(int, input().strip().split())), reverse=True)
    max_ = 0
    for i in range((N + 2) // 2):
        if N - 2 * i > A or i > B: continue

        temp = sum(A_li[:N - 2 * i]) + sum(B_li[:i])
        if max_ < temp: max_ = temp
    print(max_)