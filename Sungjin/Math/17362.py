import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    r = N % 8
    if r == 1: print(1)
    elif r == 2 or r == 0: print(2)
    elif r == 3 or r == 7: print(3)
    elif r == 4 or r == 6: print(4)
    elif r == 5: print(5)
    else: print("Error")
