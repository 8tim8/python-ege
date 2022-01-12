from itertools import product

k = 0
for i in product('СВЕТЛАН', repeat=8):
    w = ''.join(i)
    if w.count('С') == 1 and w.count('В') == 1 and w.count('Е') == 1 and \
            w.count('Т') == 1 and w.count('Л') == 1 and w.count('Н') == 1 and \
            w.count('А') == 2:
        if not 'АА' in w:
            k += 1
print(k)
