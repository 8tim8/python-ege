for s in range(10000, 1, -1):
    s1 = s
    s //= 10
    n = 1
    while s < 221:
        if n % 2 == 0:
            s += 13
        n += 5
    if n == 101:
        print(s1)
        break
