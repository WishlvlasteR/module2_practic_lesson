                                        # Исходный список чисел.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
                                        # Создаём пустые списки.
primes = []                             # Для простых чисел.
not_primes = []                         # Для не простых чисел.
for i in numbers:                       # Создаём цикл с переменной i для перебора чисел из списка numbers.
    if i == 1:                          # Если число = 1
        continue                        # Пропускаем его
    is_prime = True                     # Изначально считает число простым.
    for j in range(2, i):               # Перебирает делители от 2 до i-1.
        if i % j == 0:                  # Если делитель j найден, число не простое.
            is_prime = False            # j найден сработал флаг
            break                       # Прерывает итерацию после срабатывания флага с первым найденным делителем
    if is_prime:                        # Добавление чисел по соответствующим спискам.
        primes.append(i)                # Если значение сохранилось как True
    else:                               # Иначе
        not_primes.append(i)            # Сработал флаг и True сменилось на False
                                        # Вывод результатов.
print("Список с простыми числами:    ", primes)
print("Список с не простыми числами: ", not_primes)