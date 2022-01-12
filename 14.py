a = 3 * 125**6 + 2 * 25**9 + 5**12 - 625
b = ''
while a > 0:
    b = str(a % 5) + b
    a //= 5
b = int(b)
b = str(b)
print(b.count('0'))
