# Исходный список
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Создаем пустые списки для простых и не простых чисел
primes = []
not_primes = []

# Перебираем числа в списке numbers
for num in numbers:
    # Пропускаем число 1
    if num == 1:
        continue

    # Предполагаем, что число простое
    is_prime = True

    # Проверяем делимость от 2 до num-1
    for divisor in range(2, num):
        if num % divisor == 0:
            is_prime = False  # Если есть делитель, число не простое
            break  # Выходим из внутреннего цикла, так как число не простое

    # Добавляем число в соответствующий список
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)

# Выводим результаты
print("Primes:", primes)
print("Not Primes:", not_primes)
