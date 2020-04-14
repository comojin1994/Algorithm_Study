import sys
input = sys.stdin.readline

if __name__ == '__main__':
    A, B = map(int, input().strip().split())
    C = int(input())

    H, M = divmod(C, 60)
    result_M = B + M
    result_H = A + H
    if result_M >= 60:
        result_H += 1
        result_M -= 60
    if result_H >= 24:
        result_H %= 24
    print(result_H, result_M)