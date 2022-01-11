k = 0
for i in range(10000001, 11000001):
    a = set()
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            a.add(j)
            a.add(i // j)
    mas = sorted(a)[-2:]
    if len(mas) == 2:
        if sum(mas) < 10000:
            print(sum(mas), end=' ')
            k += 1
            if k == 5:
                break
