def move(x):
    return x + 1, x + 2, x * 2


def win(x):
    return x > 32


# если "+" - выиграшная для Пети, если "-" - выиграшная для Вани
pos = [0] * 40
# выигрыш за 1 ход
for s in range(1, 32 + 1):
    if any(win(h) for h in move(s)):
        pos[s] = 1
# проигрыш за 1 ход (ответ на 19)
for s in range(1, 32 + 1):
    if pos[s] == 0 and all(pos[h] == 1 for h in move(s)):
        pos[s] = -1
print(*[(s, p) for s, p in enumerate(pos[:34])], sep='\n')
