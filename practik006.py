#«A»: Заполнить массив случайными числами и выполнить циклический сдвиг элементов массива вправо на 1 элемент. 
import random
# Создаем массив случайных чисел
array = [random.randint(1, 100) for _ in range(6)]
print("Массив:")
print(*array)
# Выполняем циклический сдвиг вправо на 1 элемент
last_elem = array.pop(-1)
array.insert(0, last_elem)
print("Результат:")
print(*array)