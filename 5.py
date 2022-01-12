for n in range(1, 1000):
    n1 = n
    n2 = str(n)
    s1 = 0
    s2 = 0
    while n1 > 0:
        if (n1 % 10) % 2 == 0:
            s1 += n1 % 10
        n1 //= 10
    n2 = n2[::-1]
    n2 = int(n2)
    n2 = str(n2)
    n = str(n)
    for i in range(len(n2)):
        if (i + 1) % 2 == 0:
            s2 += int(n[i])
    if abs(s2-s1) == 9:
        print(int(n))
        break
