def k(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    if y % 3 == 0:
        return k(x, y - 1) + k(x, y - 2) + k(x, y // 3)
    return k(x, y - 1) + k(x, y - 2)


print(k(1, 8) * k(8, 15))
