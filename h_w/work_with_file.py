import csv
import os


def open_file():
    file_path = os.path.join(os.getcwd(), "phonebook_raw.csv")
    with open(file_path) as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


def write_corrected_data_in_new_file(data):
    with open("corrected_phonebook.csv", "w+") as f:
        data_writer = csv.writer(f, delimiter=',')
        data_writer.writerows(data)
