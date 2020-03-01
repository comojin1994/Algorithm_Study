import sys
input = sys.stdin.readline

def func(N):
    if N < 3:
        print(sum(val[:N]))
        return 1

    result = [0, val[0], val[0]+val[1]]
    for i in range(3, N+1):
        result.append(max(val[i-1] + val[i-2] + result[i-3], val[i-1] + result[i-2], result[i-1]))
    print(max(result[-1], result[-2]))
    return 1

if __name__ == '__main__':
    N = int(input())
    val = [int(input()) for _ in range(N)]
    func(N)