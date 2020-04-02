import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    time = [list(map(int, input().strip().split())) for _ in range(N)]
    time = sorted(time, key=lambda x: [x[1], x[0]])
    max_ = 1
    temp_t = time[0]
    for i in range(1, N):
        if temp_t[1] <= time[i][0]:
            temp_t = time[i]
            max_ += 1
    print(max_)