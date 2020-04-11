import sys
input = sys.stdin.readline


def isVPS(S):
    S = S.replace(' ', '')
    L = []
    for x in S:
        if x not in ['(', ')', '[', ']']:
            continue
        if x == '(':
            L.append(1)
        elif x == '[':
            L.append(2)
        elif x == ')':
            if len(L) and L[-1] == 1: del L[-1]
            else: return 'no'
        elif x == ']':
            if len(L) and L[-1] == 2: del L[-1]
            else: return 'no'
    if len(L): return 'no'
    else: return 'yes'


if __name__ == "__main__":
    while True:
        s = input().replace('\n', '')
        if s == '.': break
        print(isVPS(s))
