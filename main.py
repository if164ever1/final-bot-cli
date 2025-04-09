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
            raise ValueError("Invalid date format. Use DD.MM.YYYY") + Fore.RED
        super().__init__(self.value)

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")


# Клас Record: запис для контакту
class Record:
    pass

    def add_phone(self, phone):
        pass

    def remove_phone(self, phone):
        pass

    def edit_phone(self, old_phone, new_phone):
        pass

    def add_birthday(self, birthday):
        pass

    def days_to_birthday(self):
        pass

    def __str__(self):
        pass


# Клас AddressBook
class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name:str):
        return self.data.get(name)

    def delete(self, name:str):
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError(f"Contact {name} not found.")
        
    def get_upcoming_birthdays(self, days=7):
        upcoming = []
        today = datetime.today().date()

        for record in self.data.values():
            if record.birthday:
                next_birthday = record.birthday.value.replace(year=today.year)
                if next_birthday < today:
                    next_birthday = next_birthday.replace(year=today.year+1)
                delta_days = (next_birthday - today).days
                if delta_days <= days:
                    upcoming.append(record)
                    
        return upcoming

# Для зберігання даних у файл

# serialisation

def save_data(contacts_book, notes_book, filename="data.bin"):
    with open(filename, "wb") as file:
        pickle.dump((contacts_book, notes_book), file)

# deserialisation

def load_data(filename="data.bin"):
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        from notesbook import NotesBook
        return AddressBook(), NotesBook()


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
