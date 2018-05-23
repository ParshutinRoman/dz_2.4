

import os
from pprint import pprint

migrations = os.path.dirname(os.path.abspath(__file__))
current_dir = os.path.dirname(os.path.abspath(__file__))


def get_file_list():
    files = [f for f in os.listdir(migrations) if f.endswith('.sql')]
    while len(files) > 1:
        inp = input('Введите строку:')
        new_files = []
        for file in files:
            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), file)) as f:
                text = f.read()
            if inp in text:
                new_files.append(file)
        files = new_files
        for file in files:
            print(file)
        print(len(files))



get_file_list()
