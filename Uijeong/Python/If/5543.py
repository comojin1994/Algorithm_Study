import sys

input = sys.stdin.readline

if __name__ == "__main__":
    hams = [int(input()) for _ in range(3)]
    softs = [int(input()) for _ in range(2)]
    print(min(hams) + min(softs) - 50)