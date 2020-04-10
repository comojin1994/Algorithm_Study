import sys
input = sys.stdin.readline

if __name__ == "__main__":
    k = int(input())
    L = []
    for _ in range(k):
        n = int(input())
        if n:
            L.append(n)
        else:
            del L[-1]
    print(sum(L))