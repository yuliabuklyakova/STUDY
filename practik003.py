#Напишите программу, которая получает два целых числа A и B (0 < A < B) и выводит квадраты всех натуральных чисел в интервале от A до B.
a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))
i = a
for i in range(a, b + 1):
    print(f"{i}*{i}={i*i}")
else:
    print("Введите целые числа")