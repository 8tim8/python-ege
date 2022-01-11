f = open('24.txt')
k = 0  # длина последовательности без "А"
mx = 0  # максимальное k
ke = 0  # количество "Е" в строке
b = True
while b:
    line = f.readline()
    if line == '':
        b = False
        break
    for i in line:
        if i == 'A':
            if ke > 2:
                if k > mx:
                    mx = k
            k = 0
            ke = 0
        else:
            if i == 'E':
                ke += 1
            k += 1
print(k if k > mx else mx)
