s = input()

sec = 0
for i in s:
    asc = ord(i) - 65
    if asc < 15:
        sec += asc // 3 + 3
    elif 15 <= asc < 19:
        sec += 8
    elif 19 <= asc < 22:
        sec += 9
    elif 22 <= asc < 26:
        sec += 10

print(sec)