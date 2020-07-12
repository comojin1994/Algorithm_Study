import sys
input = sys.stdin.readline

if __name__ == '__main__':
    result = 0
    for i in range(8):
        row = input().strip()
        if i % 2 == 0:
            for idx, check in enumerate(row):
                if idx % 2 == 0 and check == 'F': result += 1
        elif i % 2 != 0:
            for idx, check in enumerate(row):
                if idx % 2 != 0 and check == 'F': result += 1
    print(result)