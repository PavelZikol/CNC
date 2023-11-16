from utils_for_json import reader, reader_to_key, reader_to_txt, write
from ncn import ncn

if __name__ == "__main__":
    print("Привет я программа созданная на языке програмирования Python, я служу для того, чтоб облегчить вам работу\n")
    while True:
     print("Давайте выберем что вам необходимо\n"
      "1 - Подготовительные (основные) команды/Коды\n"
      "2 - Вывод доступных команд \n"
      "3 - Запись программы для станков с ЧПУ(В разработке)\n"
      "4 - Вывод доступных программ для станков с ЧПУ\n"
      "5 - Тестирование по кодам\n"
      "6 - Выход из программы")
     user_input = int(input("Введите что вам необходимо : "))
     if user_input == 1:
        reader(ncn)
     elif user_input == 2:
        reader_to_key(ncn)
     elif user_input == 3:
         write()
     elif user_input == 4:
         reader_to_txt()
     elif user_input == 5:
         print("В разработке")
     elif user_input == 0:
         print("Досвидания")
         break
     else:
         print("Ввод некоректных данных повторите ещё раз")
         print()
