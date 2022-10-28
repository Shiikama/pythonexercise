file = open("task data")  # Везде буду писать обьяснение происходящего
file_with_lines = file.readlines()  # Просто читаем файл по строкам
file_with_objects = []
file_with_filters = []
file_with_date = []
file_with_magnitude1 = []
final_objects = []
final_filters = []
final_date = []
final_mag1 = []
for line in file_with_lines:
    file_with_elements = (line.split('    '))  # Разделяем каждую строку по элементам, кол-во пробелов копируем из файла
    o = file_with_elements[0]  # Выделяем каждый нужный нам элемент
    f = file_with_elements[2]
    a = o.capitalize()  # Чтобы потом избавиться от дублей мы делаем одинаковыми все обьекты которые различаются лишь по
    b = f.upper()                          # большим/маленьким буквам, пробелам и прочеркам
    c = a.replace(" ", "")
    e = c.replace("_", "")
    d = b.replace(" ", "")
    file_with_objects.append(e)  # Уже отработанные эллементы собираем в новый список и убираем дубли с set
    file_with_filters.append(d)
    s = float(file_with_elements[1])
    file_with_date.append(s)
    ma1 = (file_with_elements[3])
    file_with_magnitude1.append(ma1)
first_set = set(file_with_objects)
second_set = set(file_with_filters)
print('Hello, comrade!')
print('Available objects:')
print(first_set)
print('Observations filters:')
print(second_set)
print('Please choose the name of object and filters in which you want to receive the data.')
print('Object:')
x = input()
print('Filter1:')
y = input()
print('Filter2:')
z = input()
file = open(f'{x}.dat', "w+")
file.write('       Date            HJD24...         Magnitude1    Magnitude2\n')
for i in range(0, len(file_with_date)):
    p = min(file_with_date)
    index = file_with_date.index(p)
    if x == file_with_objects[index]:
        if y == file_with_filters[index]:
            final_objects.append(file_with_objects[index])
            final_filters.append(file_with_filters[index])
            final_date.append(file_with_date[index])
            final_mag1.append(file_with_magnitude1[index])
            s = float(file_with_date[index])
            j = s + 2400000 + 32044
            g = j // 146097
            dg = j % 146097
            c = (dg // 36524 + 1) * 3 // 4
            dc = dg - c * 36524
            b = dc // 1461
            db = dc % 1461
            a = (db // 365 + 1) * 3 // 4
            da = db - a * 365
            ye = g * 400 + c * 100 + b * 4 + a
            m = (da * 5 + 308) // 153 - 2
            dy = da - (m + 4) * 153 // 5 + 122
            Y = int(ye - 4800 + (m + 2) // 12)
            M = int((m + 2) % 12 + 1)
            D1 = dy + 1
            D = int(D1 // 1)
            T = D1 % 1
            h = T * 24
            H = int(h // 1 + 12)
            mi = h % 1
            m1 = mi * 60
            Mi = int(m1 // 1)
            se = m1 % 1
            s1 = se * 60
            S = int(s1 // 1)
            if M in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
                se = str(M)
                M = '0' + se
            if D in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
                se = str(D)
                D = '0' + se
            if H in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
                se = str(H)
                H = '0' + se
            if Mi in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
                se = str(Mi)
                Mi = '0' + se
            if S in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
                se = str(S)
                S = '0' + se
            file.write(f'{Y}.{M}.{D} {H}:{Mi}:{S}   {file_with_date[index]}    {file_with_magnitude1[index]}')
        if z == file_with_filters[index]:
            final_objects.append(file_with_objects[index])
            final_filters.append(file_with_filters[index])
            final_date.append(file_with_date[index])
            final_mag1.append(file_with_magnitude1[index])
            s = float(file_with_date[index])
            j = s + 2400000 + 32044
            g = j // 146097
            dg = j % 146097
            c = (dg // 36524 + 1) * 3 // 4
            dc = dg - c * 36524
            b = dc // 1461
            db = dc % 1461
            a = (db // 365 + 1) * 3 // 4
            da = db - a * 365
            ye = g * 400 + c * 100 + b * 4 + a
            m = (da * 5 + 308) // 153 - 2
            dy = da - (m + 4) * 153 // 5 + 122
            Y = int(ye - 4800 + (m + 2) // 12)
            M = int((m + 2) % 12 + 1)
            D1 = dy + 1
            D = int(D1 // 1)
            T = D1 % 1
            h = T * 24
            H = int(h // 1 + 12)
            mi = h % 1
            m1 = mi * 60
            Mi = int(m1 // 1)
            se = m1 % 1
            s1 = se * 60
            S = int(s1 // 1)
            if M in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
                se = str(M)
                M = '0' + se
            if D in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
                se = str(D)
                D = '0' + se
            if H in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
                se = str(H)
                H = '0' + se
            if Mi in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
                se = str(Mi)
                Mi = '0' + se
            if S in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
                se = str(S)
                S = '0' + se
            file.write(f'{Y}.{M}.{D} {H}:{Mi}:{S}   {file_with_date[index]}             {file_with_magnitude1[index]}')
    file_with_objects.remove(file_with_objects[index])
    file_with_filters.remove(file_with_filters[index])
    file_with_magnitude1.remove(file_with_magnitude1[index])
    file_with_date.remove(file_with_date[index])
file.close()
file = open(f'{x}.dat')
file_contents = file.read()
print(file_contents)
