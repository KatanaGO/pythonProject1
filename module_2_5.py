def get_matrix(n, m, value):
    # Если n или m меньше или равно 0, возвращаем пустой список
    if n <= 0 or m <= 0:
        return []

    # Создаем пустой список для матрицы
    matrix = []

    # Внешний цикл для создания строк
    for i in range(n):
        # Создаем новую строку
        row = []

        # Внутренний цикл для добавления значений в строку
        for j in range(m):
            row.append(value)  # Заполняем строку значением value

        # Добавляем строку в матрицу
        matrix.append(row)

    # Возвращаем созданную матрицу
    return matrix


# Примеры вызовов функции
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

# Выводим результаты на экран
print(result1)
print(result2)
print(result3)
