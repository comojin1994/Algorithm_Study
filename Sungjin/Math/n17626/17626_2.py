import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    result = [4 for _ in range(50001)]
    for i in range(223):
        result[i**2] = 1
        if i**2 == n: print(1); sys.exit(0)

    for i in range(1, int((n//2)**0.5) + 1):
        for j in range(1, int((n-i*i)**0.5) + 1):
            if i*i + j*j > n: continue
            elif i*i + j*j == n: print(2); sys.exit(0)
            elif (n - i*i - j*j)**0.5 % 1 == 0:
                result[n] = min(result[n], 3)
    print(result[n])