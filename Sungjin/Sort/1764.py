import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    d = {input().strip() for _ in range(N)}
    b = {input().strip() for _ in range(M)}
    result = list(d&b)
    result = sorted(result)
    print(len(result))
    for s in result:
        print(s)