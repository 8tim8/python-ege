def move(h):
    x, y = h
    return (x - 1, y), (x // 2, y), (x, y - 1), (x, y // 2)


def win(h):
    return sum(h) <= 17


size = 150
pos = [[0 for _ in range(size)] for _ in range(size)]
# win 1
for i in range(size):
    for j in range(size):
        if any(win(h) for h in move((i, j))):
            pos[i][j] = 1
# lose 1
for i in range(size):
    for j in range(size):
        if pos[i][j] == 0 and all(pos[x][y] == 1 for x, y in move((i, j))):  # но при решении 19 меняем all на any
            pos[i][j] = -1
# win 2
for i in range(size):
    for j in range(size):
        if pos[i][j] == 0 and any(pos[x][y] == -1 for x, y in move((i, j))):
            pos[i][j] = 2
# lose 2
for i in range(size):
    for j in range(size):
        if pos[i][j] == 0 and all(pos[x][y] > 0 for x, y in move((i, j))):
            pos[i][j] = -2
print(*enumerate(pos[19][:70]), sep='\n')
