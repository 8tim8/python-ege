a = []
for n in range(201, 300):
    s = '1' * n
    while '1111' in s:
        s = s.replace('1111', '22', 1)
        s = s.replace('222', '1', 1)
    a.append(s.count('1'))
print(a.index(max(a)) + 201)
