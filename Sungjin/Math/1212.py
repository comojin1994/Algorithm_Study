import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input(), 8)
    print(bin(N)[2:])