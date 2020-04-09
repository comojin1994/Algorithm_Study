import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    val = list(map(int, input().strip().split()))
    idx = val.index(-1)
    left_min = min(val[:idx])
    right_min = min(val[idx+1:])
    print(left_min + right_min)