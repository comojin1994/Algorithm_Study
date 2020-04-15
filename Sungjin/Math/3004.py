import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    if N % 2 == 0:
        print(((N//2) + 1) ** 2)
    else:
        print(((N // 2) + 1) * ((N // 2) + 2))
'''
1: 2 1*2
2: 4 2*2
3: 6 2*3
4: 9 3*3
5: 12 3*4
'''