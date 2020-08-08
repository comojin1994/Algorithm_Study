import sys
input = sys.stdin.readline

if __name__ == '__main__':
    S1 = list(input().strip())
    S2 = list(input().strip())
    cnt = 0
    for s in S1:
        if s in S2:
            cnt += 1
            S2.remove(s)
    print(len(S1) - cnt + len(S2))