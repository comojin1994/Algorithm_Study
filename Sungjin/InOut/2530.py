import sys
input = sys.stdin.readline

if __name__ == '__main__':
    A, B, C = map(int, input().strip().split())
    D = int(input())
    H, D = divmod(D, 3600)
    M, D = divmod(D, 60)
    result_H, result_M, result_S = A + H, B + M, C + D
    if result_S >= 60:
        result_M += 1
        result_S %= 60
    if result_M >= 60:
        result_H += 1
        result_M %= 60
    if result_H >= 24:
        result_H %= 24
    print(result_H, result_M, result_S)