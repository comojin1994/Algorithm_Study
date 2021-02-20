import sys
input = sys.stdin.readline

if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())


'''
10 line

Red
1 : {2, 3, 4, 5}
2 : {1, 5}
3 : {1, 5}
4 : {1, 5}
5 : {1, 2, 3, 4}

Blue
1 : {}
2 : {3, 4}
3 : {2, 4}
4 : {2, 3}
5 : {}
'''