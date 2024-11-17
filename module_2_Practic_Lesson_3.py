                                            # Исходные данные
my_list = [42,69,322,13,0,99,-5,9,8,7,-6,5] # Создан список
index = 0                                   # присвоен начальный индекс 0
while index < len(my_list):                 # Создание цикла while
    if my_list[index] == 0:                 # Если число равно 0
        index = index + 1                   # Увеличивает ndex на 1
        continue                            # Пропускает 0
    elif my_list[index] < 0:                # Если число отрицательное
        break                               # Прерывает цикл
    print(my_list[index])                   # Выводим положительное число
    index = index + 1                       # Увеличиваем индекс