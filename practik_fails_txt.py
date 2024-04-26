#Создание файла в папке Study
my_file = open("myFile.txt", "w+")
my_file.write("Привет, файл! ")
my_file.close()
#Добавление информации в файл
my_file = open("myFile.txt", "a+")
my_file.write("Добавляем новый текст")
my_file.close()
#Чтение данных из созданного нами файла
my_file = open("myFile.txt", "a+")
file_contents == my_file.read()
print(file_contents)