def endNumber(n):
    endNum = 666
    while n != 0:
        if '666' in str(endNum):
            n -= 1
        endNum += 1
    return endNum


if __name__ == "__main__":
    n = int(input())
    print(endNumber(n) - 1)