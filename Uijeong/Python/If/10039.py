import sys
input = sys.stdin.readline

if __name__ == "__main__":
    L = []
    for _ in range(5):
        num = int(input())
        if num < 40:
            num = 40
        L.append(num)
    print(sum(L)//len(L))