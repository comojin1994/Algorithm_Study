import sys
input = sys.stdin.readline

N = int(input())
mem = []

for i in range(N):
    info = []
    age, name = input().strip().split()
    info.append(int(age))
    info.append(name)
    info.append(i)
    mem.append(info)
mem = sorted(mem, key=lambda x: (x[0],x[2]))

for age, name, _ in mem:
    print(age, name)