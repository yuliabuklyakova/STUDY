#Задача A (Python 1 сл.123)
a=int(input("Введите первое целое число: "))
b=int(input("Введите второе целое число: "))
c=int(input("Введите третье целое число: "))
m=max(a,b,c)
print ("Максимальное число", m)

#Задача B (Python 1 сл.123)
a=input("Введите 5 чисел через пробел: ").split()
m=max(a)
print ("Максимальное число", m)

#Задача C (Python 1 сл.124) Ввести последовательно возраст Антона, Бориса и Виктора. Определить, кто из них старше.
A=int(input("Возраст Антона: "))
B=int(input("Возраст Бориса: "))
V=int(input("Возраст Виктора: "))
if B>A and B>V:
   print ("Борис старше всех")