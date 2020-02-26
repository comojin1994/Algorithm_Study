import sys

input = sys.stdin.readline


if __name__ == "__main__":
    while True:
        disL = list(map(int, input().split()))
        if disL[0] == 0 and disL[1] == 0 and disL[2] == 0:
            break
        h = max(disL)
        disL = list(filter(lambda x: x != h, disL))

        if h**2 != disL[0]**2 + disL[1]**2:
            print("wrong")
        else:
            print("right")
