def generate_password(n):
    if n < 3 or n > 20:
        return "Введите число от 3 до 20."

    password = ""
    for a in range(1, n):
        for b in range(a + 1, n + 1):
            pair_sum = a + b
            if n % pair_sum == 0:
                password += f"{a}{b}"

    return password

# Ввод числа от пользователя
try:
    n = int(input("Введите число от 3 до 20: "))
    result = generate_password(n)
    print(f"Пароль для {n}: {result}")
except ValueError:
    print("Пожалуйста, введите корректное целое число.")

