import sys
input = sys.stdin.readline

if __name__ == '__main__':
    num = int(input().strip(), 2) * 17
    print(str(bin(num))[2:])