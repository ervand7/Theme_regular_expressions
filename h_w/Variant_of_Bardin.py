from typing import Optional, List
from chardet.universaldetector import UniversalDetector
import re
import csv


class ContactNormalizer:
    # Наборы паттернов - можно расширять как угодно, ключи помогут не потеряться, что парсим
    patterns = {
        'fio': {
            'regexp': r'\b([А-Я]\w+)\s*,*([А-Я]\w+)\s*,*([А-Я]\w+\s*)*',
            'subst': r"\1, \2, \3"
        },
        'phone': {
            'regexp': r'(\+7\s*|8\s*)\(*(\d{3})\)*\s*-*(\d{3})-*\s*(\d{2})-*\s*(\d{2})',
            'subst': r'+7(\2)\3-\4-\5'},
        'add_phone': {
            'regexp': r'\(*(\b[д][о][б])\s*(\.*)\s*(\w+)\)*',
            'subst': r'\1\2\3'
        }
    }

    def __init__(self, source_file_csv, target_file_csv='parsed_file.csv', delimiter=None, is_save_parsed_file=True):
        """
        Инициализация
        :param source_file_csv: пусть к файлу CSV (источнику с неправильными данными)
        :param delimiter: разделитель
        :param is_save_parsed_file: нужно ли сохранять новый файл с обработанными данными
        :param target_file_csv: путь к новому файлу
        """
        DELIMITER = ','

        self.file = source_file_csv
        self.parsed_csv_file_path = target_file_csv
        self.is_save_parsed_file = is_save_parsed_file
        self.delimiter = delimiter or DELIMITER
        self.encoding = 'utf-8'
        self.parsed_data = {}

    def detect_encoding(self):
        """
        Метод определения кодировки
        :return: кодировка
        """
        detector = UniversalDetector()
        with open(self.file, 'rb') as file:
            for line in file.readlines():
                detector.feed(line)
                if detector.done:
                    break
        detector.close()
        self.encoding = detector.result['encoding']
        return self.encoding

    def get_initial_data_list(self) -> Optional[List[List]]:
        """
        Метод для получения сырых данных
        :return: список списков
        """
        try:
            with open(self.file, encoding=self.detect_encoding()) as f:
                rows = csv.reader(f, delimiter=self.delimiter)
                return list(rows)
        except FileNotFoundError:
            print('Файл не найден')
            return None

    def create_and_write_in_new_csv_file(self):
        """
        Создание нового файла. Потом в этот файл будем прописывать исправленные данные
        """
        if self.parsed_data:
            with open(self.parsed_csv_file_path, "w", encoding=self.encoding) as file:
                data_writer = csv.writer(file, delimiter=self.delimiter)
                data_writer.writerows([self.parsed_data[key] for key in self.parsed_data])

    def parse_data(self, row_data: List[str]) -> List[str]:
        """
        Парсинг данных и обработка согласно набору паттернов
        :param row_data: данные для парсинга - список
        :return: список с данными
        """
        row_data = ','.join(row_data)
        for key, patten in self.patterns.items():
            row_data = re.sub(patten['regexp'], patten['subst'], row_data)
        return row_data.split(',')

    def check_data(self, row_data: List[str], unique_key_index: int = 0):
        """
        Проверка данных на уникальность
        :param row_data:
        :param unique_key_index: какое поле ключа используем как уникальный идентификатор
        """
        data_id = row_data[unique_key_index]

        if self.parsed_data.get(data_id):
            old_data = self.parsed_data.get(data_id)

            for index, data in enumerate(old_data):
                for new_index, new_data in enumerate(row_data):
                    if new_index == index and not data and new_data:
                        old_data[index] = new_data
        else:
            self.parsed_data[data_id] = row_data

    def start_parse(self):
        """
        Старт парсиннга
        :return: данные парсинга или ничего
        """
        contacts_list = self.get_initial_data_list()
        if contacts_list:
            for contact in contacts_list:
                self.check_data(self.parse_data(contact))

            if self.is_save_parsed_file:
                self.create_and_write_in_new_csv_file()

            return self.parsed_data

        return None


if __name__ == '__main__':
    ContactNormalizer('phonebook_raw.csv').start_parse()
