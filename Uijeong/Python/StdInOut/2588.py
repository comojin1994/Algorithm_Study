a = int(input())
b = int(input())

temp = b
for i in range(len(str(b))):
    print(a * (temp % 10))
    temp = temp // 10
print(a * b)