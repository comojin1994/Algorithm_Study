s = input()

alpha = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

cnt = 0
for a in alpha:
    cnt += s.count(a)
    s = s.replace(a, ' ')

s = s.replace(' ', '')
cnt += len(s)

print(cnt)