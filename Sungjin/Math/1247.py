import sys
input = sys.stdin.readline

def check(N):
    if N == 0: return "0"
    elif N < 0: return "-"
    elif N > 0: return "+"
    else: return "Error"

if __name__ == '__main__':
    for _ in range(3):
        N = int(input())
        total = 0
        for _ in range(N):
            total += int(input())
        print(check(total))