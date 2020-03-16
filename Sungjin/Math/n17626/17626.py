import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    min_ = 4
    for i in range(int(n**0.5), int((n//4)**0.5), -1):
        if i*i ==n: min_ = 1; break
        else:
            temp = n - i*i
            for j in range(int(temp**0.5), int((temp//3)**0.5), -1):
                if i*i + j*j == n: min_ = min(min_, 2); continue
                else:
                    temp = n - i*i - j*j
                    for k in range(int(temp**0.5), int((temp//2)**0.5), -1):
                        if i*i + j*j + k*k == n: min_ = min(min_, 3)
    print(min_)