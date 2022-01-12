import math

f = open('17.txt')
k = 0
sr = 0
b = True
while b:
    line = f.readline()
    if line == '':
        b = False
        break
    x = int(line)
    if x % 2 == 0:
        sr += x
        k += 1
sr //= k
k = 0
ms = 0
b = True
f = open('17.txt')
x = int(f.readline())
while b:
    line = f.readline()
    if line == '':
        b = False
        break
    y = int(line)
    if (x % 3 == 0 or y % 3 == 0) and (x < math.trunc(sr) or y < math.trunc(sr)):
        k += 1
        ms = max(ms, x + y)
    x = y
print(k, ms)
