import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    seq = [int(input()) for _ in range(n)]
    result = []
    cur = 0; bp = False
    for n in seq:
        if n > cur:
            for i in range(cur + 1, n + 1):
                seq.append(i)
                result.append('+')
            cur = n
            if n == seq.pop(): result.append('-')
            else: print('No'); exit(0)
        else:
            if n == seq.pop(): result.append('-')
            else: print('NO'); exit(0)
    for n in result:
        print(n)