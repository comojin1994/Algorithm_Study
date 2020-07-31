import sys
input = sys.stdin.readline

if __name__ == '__main__':
    m = int(input())
    ball = [0, 1, 0, 0]
    for _ in range(m):
        a, b = map(int, input().strip().split())
        temp = ball[a]
        ball[a] = ball[b]
        ball[b] = temp
    print(ball.index(1))