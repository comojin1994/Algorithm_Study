import sys
input = sys.stdin.readline


def isVPS(s):
    L = []
    for x in s:
        if x == '(':
            L.append(1)
        else:
            if not len(L):
                return 'NO'
            else:
                del L[-1]
    return 'YES' if not len(L) else 'NO'


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        S = input().strip()
        print(isVPS(S))
