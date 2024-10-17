# Ввод трех целых чисел
print("Введите число: ")
first = int(input())
second = int(input())
third = int(input())

# Условная конструкция для определения количества одинаковых чисел
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)