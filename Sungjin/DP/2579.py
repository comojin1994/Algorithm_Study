import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    val = [int(input()) for _ in range(N)]
    result = [val[0], val[0] + val[1], max(val[0]+val[2], val[1]+val[2])]

    for i in range(3, N):
        result.append(max(val[i] + val[i-1] + result[i-3], val[i] + result[i-2]))
    print(result[-1])