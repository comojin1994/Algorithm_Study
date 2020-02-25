dial = input()
time = [t+1 for t in range(11)]
a = {chr(ord('A') + i) : 2+i // 3 for i in range(ord('Z')-ord('A')+1)}
a['S'] = 7
a['V'] = 8
a['Y'] = 9
a['Z'] = 9

total = 0
for i in dial:
    total += time[a[i]]
print(total)