s = []
for a1 in range(1, 101):
    for a2 in range(1, 101):
        fl = True
        for x in range(1, 101):
            if not(not(4 <= x <= 51) or (19 <= x <= 84) or (a1 <= x <= a2)):
                fl = False
                break
        if fl:
            s.append(a2 - a1)
print(min(s)+1)
