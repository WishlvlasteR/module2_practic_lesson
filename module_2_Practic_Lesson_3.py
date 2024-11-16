# Исходные данные
my_list = [42,69,322,13,0,99,-5,9,8,7,-6,5]

# Начальный индекс
index = 0

# Цикл while
while index < len(my_list):
    # Если число отрицательное, прерываем цикл
    if my_list[index] < 0:
        break
    # Если число равно 0, пропускаем его
    elif my_list[index] == 0:
        index = index + 1
        continue
    # Выводим положительное число
    print(my_list[index])
    # Увеличиваем индекс
    index = index + 1