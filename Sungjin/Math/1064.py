import sys
input = sys.stdin.readline

def getlen(x, y):
    return (((x[0] - y[0]) ** 2) + ((x[1] - y[1]) ** 2)) ** (0.5)

if __name__ == '__main__':
    xa, ya, xb, yb, xc, yc = map(int, input().strip().split())
    dist = [getlen([xa, ya], [xb, yb]),
            getlen([xb, yb], [xc, yc]),
            getlen([xc, yc], [xa, ya])]

    if (xb - xa) * (yc - ya) == (yb - ya) * (xc - xa): print(-1)
    else:
        result = [2 * (dist[0] + dist[1]),
                  2 * (dist[1] + dist[2]),
                  2 * (dist[2] + dist[0])]
        print(max(result) - min(result))