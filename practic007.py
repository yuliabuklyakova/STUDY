#Необходимо найти и вывести на экран строку с максимальной длиной.
words = ['Москва', 'Нижний Новгород', 'Элиста', 'яблоко']
#создаем пустую строку для хранения самого длинного слова
max_word = ''
for word in words: #перебираем строки в списке
    if len(word) > len(max_word): #если длина текущей строки больше 
        max_word = word #обновляем значение переменной
print(max_word) #выводим итоговое значение на экран


words = ['четыре', 'восемь', 'пятнадцать', 'восемнадцать']
max_word = max(words)
print(max_word)


words = ['четыре', 'восемь', 'пятнадцать', 'восемнадцать']
#внутри max() прописываем параметр key для поиска слова с максимальной длиной 
max_word = max(words, key=len)
print(max_word)