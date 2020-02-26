s = input().upper()

L = list(set(s))

countL = [s.count(i) for i in L]

if countL.count(max(countL)) == 1:
    print(L[countL.index(max(countL))])
else:
    print("?")