import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    power = list(map(int, input().strip().split()))
    last = sum(power) // 2
    idx = power.index(last)
    val = power.pop(idx)
    power.append(val)
    print(' '.join(map(str, power)))