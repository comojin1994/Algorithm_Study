import sys
input = sys.stdin.readline

if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0: break
        text = [list(input()) for _ in range(n)]
        idx = 0
        for line in text:
            if idx > len(line): continue
            for idx in range(idx, len(line)):
                if line[idx] == ' ' or line[idx] == '\n': break
        print(idx+1)