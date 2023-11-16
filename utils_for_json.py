def reader(file):
    while True:
        user_input_2 = input("Напишите необходимое вам слово или словосочетание,\nТак же вы можете обозначить ключевые слова в том слове, которое вам необходимы\nТак же вы можете выйти из программы нажав 0 : ")
        user = user_input_2.capitalize()
        for key, value in file.items():
            if user in key:
                print()
                print(key, value)
                print()
        if user == "0":
            print("Спасибо за ознакомление с возможностями")
            print()
            break


def reader_to_key(file):
    for i, a in file.items():
        print(f"Функция : {i}")
        print(a)
        print()

def write():
    while True:
        print("Вы выбрали запись программы для станка с ЧПУ")
        user_input = input("Если вы хотите выйти нажмите 0\nЕсли вы хотите продолжить нажмите 1 : ")
        if user_input == "0":
         break
        elif user_input == "1":
            user_program = input("Напишите как будет называться ваша программа : ")
            key = user_program.capitalize()
            print(key)
            print()
            user_insert = input("Напишите вашу программу : ")
            value = user_insert
            with open("NCN.txt", "a", encoding="utf:8") as f:
                f.write(f"{key}:{value.split()}\n")

        else:
            print("Некоректный ввод")
            print()

def reader_to_txt():
    while True:
        user = input("1 для отображения программы\n0 для выхода из программы : ")
        if user == "0":
            break
        elif user == "1":
            with open("NCN.txt", "r", encoding="utf:8") as f:
                print(f.read())
                break
        else:
            print("Некоректный ввод")

def teasting(file):
    count = 0
    user_input = input("Готовы ли вы пройти тестирование?\n"
          "1 - да\n"
          "0 - Пока нет, давайте попозже")
    while count == 5:
        count = 0
        for key, value in file:
            print(value)
            print("Напишите G код который подходит под описание")





