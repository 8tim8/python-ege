def f(num):
    if num == 0:
        return 0
    if num > 0:
        if num % 3 == 2:
            return f(num - 1) + 1
        if num % 3 < 2:
            return f((num - num % 3) // 3)


for n in range(1, 1000):
    if f(n) == 6:
        print(n)
        break
