def get_matrix(n, m, value):                                  # Создаёт функцию с переменной get_matrix с 3 значениями
    matrix=[]                                                 # Создаёт вложенный в функцию get_matrix пустой список
    for i in range(n):                                        # Проходит по индексам которые указаны  в result_1,2,3(n)
        list_1=[]                                             # Создает пустой лист для записи в него значения :value
        for j in range(m):                                    # Проходит по индексам которые указаны  в result_1,2,3(m)
            list_1.append(value)                              # Добавляет значение value в list_1
        matrix.append(list_1)                                 # Добавляет все значения списка list_1 в список matrix
    return matrix                                             # Возвращает переменную Matrix
result_1=get_matrix(2,3,4)                        # Создаёт дублирующую переменную №1 от get_matrix
result_2=get_matrix(3,4,5)                        # Создаёт дублирующую переменную №2 от get_matrix
result_3=get_matrix(4,5,6)                        # Создаёт дублирующую переменную №3 от get_matrix
print('Вывожу результат № 1: ', result_1)                      # Выводит результат 1
print('Вывожу результат № 2: ', result_2)                      # Выводит результат 2
print('Вывожу результат № 3: ', result_3)                      # Выводит результат 3


