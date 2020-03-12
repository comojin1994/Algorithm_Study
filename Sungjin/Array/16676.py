import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    num = [0, 11, 111, 1111, 11111, 111111, 1111111, 11111111, 111111111, 1111111111]
    for i in range(9):
        if num[i] <= N < num[i+1]: print(i+1); break