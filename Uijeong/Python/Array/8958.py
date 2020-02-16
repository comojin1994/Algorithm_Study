n = int(input())

for i in range(n):
    oxL = input()
    score, total = 0, 0
    for ox in oxL:
        if ox == 'O':
            score += 1
        else:
            score = 0
        total += score
    print(total)