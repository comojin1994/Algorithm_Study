import sys
input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        d = {}
        cnt = 1
        for _ in range(n):
            name, category = input().strip().split()
            d[category] = d[category] + 1 if category in d else 2
        for key, value in d.items():
            cnt *= value
        print(cnt - 1)
