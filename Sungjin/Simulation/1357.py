import sys
input = sys.stdin.readline

def getReversed(X):
    return int(''.join(list(reversed(X))))

if __name__ == '__main__':
    X, Y = input().strip().split()
    XY = str(getReversed(X) + getReversed(Y))
    print(getReversed(XY))