import sys
input = sys.stdin.readline

def check(str):
    a = []
    for s in str:
        if s == '(' or s == '[':
            a.append(s)
        elif s == ')':
            if len(a) == 0:
                return False
            if a[-1] == '(':
                a.pop()
            else:
                return False
        elif s == ']':
            if len(a) == 0:
                return False
            if a[-1] == '[':
                a.pop()
            else:
                return False
    if len(a) == 0:
        return True
    else: return False


if __name__ == '__main__':
    while True:
        str = input().rstrip()
        if str == '.':
            break
        str = list(str)
        if check(str):
            print('yes')
        else:
            print('no')