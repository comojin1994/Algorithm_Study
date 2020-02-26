n = int(input())
cnt = 0

for i in range(n):
    s = input()

    if list(s) == sorted(s, key=s.find):
        cnt += 1

print(cnt)