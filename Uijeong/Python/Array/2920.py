import sys

input = sys.stdin.readline


if __name__ == "__main__":
    L = list(map(int, input().split()))
    aFlag, dFlag = True, True

    for i, num in enumerate(L):
        if num != i+1:
            aFlag = False
        if num != 8-i:
            dFlag = False

    if aFlag:
        print("ascending")
    elif dFlag:
        print("descending")
    else:
        print("mixed")
