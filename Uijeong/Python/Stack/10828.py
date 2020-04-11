import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    L = []
    for _ in range(n):
        line = input().strip().split()
        operator = line[0]
        if operator == "push":
            L.append(line[1])
        elif operator == "pop":
            if len(L):
                print(L[-1])
                del L[-1]
            else:
                print(-1)
        elif operator == "size":
            print(len(L))
        elif operator == "empty":
            print(1 if not len(L) else 0)
        elif operator == "top":
            print(L[-1] if len(L) else -1)