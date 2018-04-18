# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os
from pprint import pprint

migrations = os.path.dirname(os.path.abspath(__file__))
current_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    # ваша логика
    def get_file_list():
        files = [f for f in os.listdir(migrations) if f.endswith('.sql')]
        while True:
            inp = input('Введите строку:')
            for file in files:
                with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), file)) as f:
                    text = f.read()
                if inp not in text:
                    files.remove(file)
            pprint(files)
            print(len(files))



    '''def get_file_list():
        files = [f for f in os.listdir(migrations) if f.endswith('.sql')]
        for file in files:
            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), file)) as f:
                text = f.read()
            inp = 'INSERT'
            inp = inp.lower()
            if inp not in text:
               files.remove(file)
        pprint(files)
        print(len(files))

    def open_file():
        get_file_list()
        for file in files:
            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), file)) as f:
                print(f.read())'''

    get_file_list()
