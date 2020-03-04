import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    C = [0] * 10001

    # count
    for _ in range(n):
        a = int(input())
        C[a] = C[a] + 1
    # rearrange
    for j in range(len(C)):
        print(f'{j}\n' * C[j], end='') # f-string

