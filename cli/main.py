from collections import UserDict
from datetime import datetime
import pickle
from colorama import Fore, Style, init
import re


# Клас для базового поля (Field) і його наслідування
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not re.match(r'^\+?\d{10,15}$', value):
            raise ValueError("Invalid phone number format") + Fore.RED
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(self.value)

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")




# Для зберігання даних у файл

# serialisation

def save_data():
    pass


# deserialisation

def load_data():
    pass


# Декоратор для обробки помилок
def input_error(func):
    pass


# Команди для роботи з адресною книгою
@input_error
def add_contact(args, book: AddressBook):
    pass


@input_error
def change_phone(args, book: AddressBook):
    pass


@input_error
def show_phones(args, book: AddressBook):
    pass


@input_error
def show_all(book: AddressBook):
    pass


@input_error
def add_birthday(args, book: AddressBook):
    pass


@input_error
def birthdays(args, book: AddressBook):
    pass


# Функція для обробки команд
def parse_input():
    pass


# Головна функція для запуску програми
def main():
    pass


if __name__ == "__main__":
    main()
