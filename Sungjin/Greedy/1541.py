import sys
input = sys.stdin.readline

if __name__ == '__main__':
    equ = input().strip().split('-')
    result = 0
    for i in range(len(equ)):
        temp = equ[i].split('+')
        temp_sum = 0
        for t in temp:
            temp_sum += int(t)
        if i == 0: result += temp_sum
        else: result -= temp_sum
    print(result)