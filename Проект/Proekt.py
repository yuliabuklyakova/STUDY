#Создание опросника
#Приветственное сообщение
def message():
    print("Добрый день! Пожалуйста, ответьте на несколько вопросов!")
    print("                       **********                     ")
    #Запускаем первый вопрос
def question1():
    answer = input("С помощью какого оператора функция возвращает результат?")
    if answer.casefold() == "return":
        print("👍Правильный ответ!")
        return True
    else:
        print("👎Подумайте еще!")
        return False
#Запускаем второй вопрос
def question2():
    answer = input("Какая команда позволяет подключить библиотеку?")
    if answer.casefold() == "import":
        print("👍Правильный ответ!")
        return True
    else:
        print("👎Подумай еще!")
        return False
#Запуск опросника с подсчетом правильных ответов
def run_quiz():
    number = 0
    message()
    if question1():
        number +=1
    if question2():
        number +=1
    print("Из двух вопросов вы ответили правильно на", number, "вопрос/ов")
    return("Из двух вопросов вы ответили правильно на", number, "вопрос/ов")
run_quiz()