import sys
input = sys.stdin.readline

def func(N):
    if N == 1:
        print(val[0])
        return 1
    elif N == 2:
        print(val[0] + val[1])
        return 1
    elif N == 3:
        print(max(val[0] + val[2], val[1] + val[2], val[0] + val[1]))
        return 1

    result = [val[0], val[0] + val[1], max(val[0] + val[2], val[1] + val[2])]

    for i in range(3, N):
        a = max(result[:i-2])
        b = max(a, result[i-2])
        result.append(max(a + val[i-1] + val[i], b + val[i]))
    print(max(result[-1], result[-2]))

    return 1

if __name__ == '__main__':
    N = int(input())
    val = [int(input()) for _ in range(N)]
    func(N)