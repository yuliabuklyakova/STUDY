#Ввести с клавиатуры в одну строку фамилию, имя и отчество, разделив их пробелом. Вывести фамилию и инициалы.
strFIO = "Иванов Петр Семенович"
listFIO = strFIO.split(" ")
strNewFIO = listFIO[1][:1] + "." + listFIO[2][:1] + ". " + listFIO[0]
print(strNewFIO)