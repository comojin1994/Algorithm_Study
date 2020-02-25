import math

def fraction(x):
    k = math.ceil(math.sqrt(2*x))
    for i in range(k, 0, -1):
        first = (i**2 - i)//2
        last = (i**2 + i)//2
        if first < x <= last:
            if i % 2 == 1:
                a = i - x + first + 1
                b = x - first
            else:
                a = x - first
                b = i - x + first + 1
            return a, b


if __name__ == "__main__":
    x = int(input())
    a, b = fraction(x)
    print("{}/{}".format(a, b))