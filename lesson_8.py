'''
#  Погружение в Python (семинары)
## Урок 8. Сериализация

###  Задание 1
Напишите функцию, которая получает на вход директорию 
и рекурсивно обходит её и все вложенные директории. 
Результаты обхода сохраните в файлы json, csv и pickle. 
Для дочерних объектов указывайте родительскую директорию. 
Для каждого объекта укажите файл это или директория. 
Для файлов сохраните его размер в байтах, а для директорий размер файлов 
в ней с учётом всех вложенных файлов и директорий.
'''

import csv
import json
from pathlib import Path
import pickle

__all__ = [
    'serialization_files'
]


def serialization_files(directory: Path):
    data = {}
    for i in directory.rglob('*'):
        size = 0
        if i.is_dir():
            for file in i.rglob('*'):
                size += file.stat().st_size
        else:
            size = i.stat().st_size

        data[i.name] = {
            'parent': i.parent.name,
            'type': 'directory' if i.is_dir() else 'file',
            'size': size
        }

    with open(Path(directory, 'json_data.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    with open(Path(directory, 'pickle_data.pickle'), 'wb') as f:
        pickle.dump(data, f)

    with open(Path(directory, 'csv_data.csv'), 'w', newline='', encoding='utf-8') as f:
        csv_writer = csv.writer(f)
        header = ['file', 'parent', 'type', 'size']
        csv_writer.writerow(header)

        for key, value in data.items():
            line = [key]
            values = [val for val in value.values()]
            line.extend(values)
            csv_writer.writerow(line)


if __name__ == '__main__':
    serialization_files(Path('/Users/'))