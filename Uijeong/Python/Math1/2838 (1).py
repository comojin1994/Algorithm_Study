def sugar(weight):
    if weight % 5 == 0: return weight // 5

    max = weight // 3

    for i in range(1, max + 1):
        if (weight - i * 3) % 5 > 0:
            continue
        return i + (weight - i * 3) // 5
    return -1


if __name__ == "__main__":
    w = int(input())
    print(sugar(w))
