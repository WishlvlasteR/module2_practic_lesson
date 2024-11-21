def generate_password(n):
    result = ""                                         # Строка для хранения результата
    for i in range(1, n):                               # Первое число пары
        for j in range(i + 1, n):                       # Второе число пары
            if n % (i + j) == 0:                        # Проверяем кратность суммы пары
                result += str(i) + str(j)               # Добавляем пару в результат
    return result


n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    passw = generate_password(n)
    print("Для пароля из числа:", n, "Подобран пароль:", passw)
else:
    print("Число должно быть от 3 до 20.")
