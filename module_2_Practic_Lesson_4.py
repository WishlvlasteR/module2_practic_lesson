                                        # Исходный список чисел.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
                                        # Создаёт пустые списки.
primes = []                             # Для простых чисел.
not_primes = []                         # Для не простых чисел.

for i in numbers:                       # Перебирает числа из списка numbers.
    if i == 1:
        continue                        # Пропускает число 1.

    is_prime = True                     # Изначально считает число простым.

    for j in range(2, i):               # Перебирает делители от 2 до i-1.
        if i % j == 0:                  # Если делитель j найден, число не простое.
            is_prime = False            # j найден сработал флаг
            break                       # Прерывает итерацию после срабатывания флага и  первым найденным делителем
                                        # Добавление числа в соответствующий список.
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
                                        # Вывод результатов.
print("Список с простыми числами:    ", primes)
print("Список с не простыми числами: ", not_primes)