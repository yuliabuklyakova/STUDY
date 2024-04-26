#Практикум по регулярным выражениям: Сопоставления номера автомобиля
import re
car_number = input("Введите номер автомобиля, в формате Х123ХХ123: ")
car_number_pattern = re.compile(r'[А-Я]\d{3}[А-Я]{2}\d{2,3}')
if re.match(car_number_pattern,car_number):
    print("Да")
else:
    print("Нет")