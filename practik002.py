#«B»: Напишите программу, которая получает номер месяца и выводит соответствующее ему время года или сообщение об ошибке. 
month_number = input ("Введите номер месяца: ")
#Присваеваем переменной номер месяца с условием
if month_number == "1" or "2" or "12": 
   print("Зима.")
elif month_number == "3" or "4" or "5":
   print("Весна.")
elif month_number == "6" or "7" or "8 ":
   print ("Лето.")
elif month_number == "9" or "10" or "11":
   print ("Осень.")
else:
   print ("Неверный номер месяца.")