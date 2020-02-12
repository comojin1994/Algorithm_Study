import sys
import statistics as st
input = sys.stdin.readline

N = int(input())
num = []
cnt = {}

for _ in range(N):
    n = int(input())
    num.append(n)
    if n in cnt.keys():
        cnt[n] += 1
    else:
        cnt[n] = 1
for_mod = list(cnt.items())

s = 0
for n in sorted(cnt.keys()):
    s += cnt[n]
    cnt[n] = s

key = [0 for _ in range(N)]
for n in num:
    key[cnt[n]-1] = n
    cnt[n] -= 1

value = sorted(for_mod, key=lambda x: x[0])
value = sorted(value, key=lambda x: x[1], reverse=True)
if len(value) == 1:
    mod = value[0][0]
else:
    if value[0][1] == value[1][1]:
        mod = value[1][0]
    else:
        mod = value[0][0]

print(round(sum(key)/len(key)))
print(st.median(key))
print(mod)
print(max(key) - min(key))
