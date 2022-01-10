f = open('26.txt')
k = 0  # количество выполняемых процессов
mp = 0  # наибольшее количество одновременных процессов на неделе
t = 0  # суммарное количество секунд
x = 1633305600  # начальный момент времени
y = x + 604800  # время, в конце недели
a = []  # массив процессов, начавшихся на неделе
n = int(f.readline())  # количество процессов за весь период
for i in range(604801):
    a.append(0)  # заполняем массиво нулями
b = True
while b:  # пока не конец файла
    line = f.readline()  # считываем строку
    if line == '':  # проверяем кончился файл или нет
        b = False
        break  # если кончился, то выходим из цикла
    numbs = line.split(' ')  # разбиваем строку на отдельные числа
    new_numb = []  # создаём массив для этих чисел
    for numb in numbs:
        new_numb.append(numb)  # заполняем массив
    if '\n' in new_numb[1]:  # делаем проверку на лишние символы в строке (питон иногда их добавляет)
        new_numb[1] = new_numb[1].replace('\n', '', 1)  # удаляем ненужные символы
    p0 = int(new_numb[0])  # время старта процесса
    p1 = int(new_numb[1])  # время завершения процесса
    if (p0 < x) and ((p1 > x) or (p1 == 0)):  # процесс начался до недели и закончился после
        k += 1
    if (p0 >= x) and (p0 <= y):  # процесс начался на неделе
        a[p0 - x] += 1
    if (p1 >= x) and (p1 <= y):  # процесс закончился на неделе
        a[p1 - x] -= 1
for i in range(604801):  # начинаем перебор массива
    k += a[i]  # добавляем элементы массива к количеству процессов на неделе
    if k > mp:  # если количество процессов на неделе больше наибольшего количества процессов
        mp = k  # считаем, что это наибольшее число процессов
        t = 0  # обнуляем суммарное количество секунд
    if k == mp:  # если количество процессов на неделе равно наибольшегму количеству процессов
        t += 1  # увеличиваем количество секунд на один
print(mp, t)  # выводим требуемые в задаче значения