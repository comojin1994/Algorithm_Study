import sys

input = sys.stdin.readline


if __name__ == "__main__":
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    xL = [x1, x2, x3]
    yL = [y1, y2, y3]

    x = list(filter(lambda a: xL.count(a) == 1, list(set(xL))))
    y = list(filter(lambda b: yL.count(b) == 1, list(set(yL))))

    print(x[0], y[0])
