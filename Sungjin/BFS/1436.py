import sys
input = sys.stdin.readline

N = int(input())

word = '666'
cnt = 0
num = 666

while True:
    if word in str(num):
        cnt += 1
    if cnt == N:
        print(num)
        break
    num += 1