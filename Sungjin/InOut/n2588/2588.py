import sys
input = sys.stdin.readline

n = input().strip()
m = input().strip()

print(int(n) * int(m[2]))
print(int(n) * int(m[1]))
print(int(n) * int(m[0]))
print(int(n) * int(m))