
def top(n, s, e, l):
    if n == 1:
        print(s, e)
        return
    else:
        top(n-1, s, l, e)
        print(s, e)
        top(n-1, l, e, s)


if __name__ == "__main__":
    n = int(input())
    print(2**n - 1)
    top(n, 1, 3, 2)

