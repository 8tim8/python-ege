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
# выигрыш за 2 хода (ответ на 20)
for s in range(1, 32 + 1):
    if pos[s] == 0 and any(pos[h] == -1 for h in move(s)):
        pos[s] = 2
# проигрыш за 2 хода
for s in range(1, 32 + 1):
    if pos[s] == 0 and all(pos[h] > 0 for h in move(s)):
        pos[s] = -2
# выигрыш за 3 хода
for s in range(1, 32 + 1):
    if pos[s] == 0 and any(pos[h] < 0 for h in move(s)):
        pos[s] = 3
# проигрыш за 3 хода
for s in range(1, 32 + 1):
    if pos[s] == 0 and all(pos[h] > 0 for h in move(s)):
        pos[s] = -3
# выигрыш за 4 хода
for s in range(1, 32 + 1):
    if pos[s] == 0 and any(pos[h] < 0 for h in move(s)):
        pos[s] = 4
# проигрыш за 4 хода (ответ на 21)
for s in range(1, 32 + 1):
    if pos[s] == 0 and all(pos[h] > 0 for h in move(s)):
        pos[s] = -4
print(*[(s, p) for s, p in enumerate(pos[:34])], sep='\n')
