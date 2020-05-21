import sys
input = sys.stdin.readline

if __name__ == '__main__':
    L = int(input())
    Lucky = sorted(list(map(int, input().strip().split())))
    N = int(input())
    flag = False
    for i in range(len(Lucky)):
        if i == len(Lucky) - 1: flag = True; break
        if Lucky[i] < N and N < Lucky[i + 1]:
            break

    if flag: print(0)
    else:
        print((N - Lucky[i] - 1) + (Lucky[i + 1] - N - 1) + (N - Lucky[i] - 1) * (Lucky[i + 1] - N - 1))