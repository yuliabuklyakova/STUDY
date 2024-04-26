#Чтение данных из файла CSV

import csv

exampleFile = open('example.csv', encoding = 'UTF-8')
exampleReader = csv.reader(exampleFile, delimiter = ';')
exampleData = list(exampleReader)

print(exampleData)

exampleFile.close()
#Обращение к отдельным ячейкам/строкам
import csv

exampleFile = open('example.csv', encoding = 'UTF-8')
exampleReader = csv.reader(exampleFile, delimiter = ';')

for row in exampleReader:
    string = 'Строка 2' + str(exampleReader.line_num) + ' '
    for value in row:
        string = string + value + ' '
    print(string)

exampleFile.close()