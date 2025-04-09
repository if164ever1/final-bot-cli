from collections import UserDict
from datetime import datetime
import pickle
import re
# ---------------------------------винести в окремий файл
# Класи для управління контактами
class Field:
    pass

class Name(Field):
    pass

class Phone(Field):
    pass

class Birthday(Field):
    pass
# ------------------------------------
# -----------------------------------окремий файдл
class Record:
    def add_phone(self, phone):
        pass

    def remove_phone(self, phone):
        pass

    def edit_phone(self, old_phone, new_phone):
        pass

    def add_birthday(self, birthday):
        pass

    def add_email(self, email):
        pass

    def add_address(self, address):
        pass

    def days_to_birthday(self):
        pass
# -------------------------------------------
# --------------------------------------------окремий файл
class AddressBook(UserDict):
    def add_record(self, record):
        pass

    def find(self, name):
        pass

    def delete(self, name):
        pass

    def get_upcoming_birthdays(self, days=7):
        pass
 

# Функції для управління контактами
def add_contact(args, book: AddressBook):
    pass

def change_phone(args, book: AddressBook):
    pass

def show_phones(args, book: AddressBook):
    pass

def show_all(book: AddressBook):
    pass

def add_birthday(args, book: AddressBook):
    pass

def birthdays(args, book: AddressBook):
    pass

def edit_contact(args, book: AddressBook):
    pass
# -------------------------------------------------
# ---------------------------------------------------кремий файл
# Класи для управління нотатками
class Note:
    def add_tags(self, tags):
        pass

    def has_tag(self, tag):
        pass
# -------------------------------------------------
# ---------------------------------------------------оремий файл
class NotesBook(UserDict):
    def add_note_with_tags(self, content, tags=None):
        pass

    def delete_note(self, note_id):
        pass

    def edit_note(self, note_id, new_content):
        pass

    def search_notes_by_tag(self, tag):
        pass

    def sort_notes_by_tags(self):
        pass


# Функції для управління нотатками
def add_note(args, notes_book: NotesBook):
    pass

def delete_note(args, notes_book: NotesBook):
    pass

def edit_note(args, notes_book: NotesBook):
    pass

def search_notes(args, notes_book: NotesBook):
    pass

def add_note_with_tags(args, notes_book: NotesBook):
    pass

def search_notes_by_tag(args, notes_book: NotesBook):
    pass

def sort_notes_by_tags(notes_book: NotesBook):
    pass
# ----------------------------------------------------------------окремий файл
# Функції для інтелектуального аналізу
def suggest_command(user_input):
    pass
# -----------------------------------------------------------
# ----------------------------------------------------------окремий файл
# Серіалізація та десеріалізація
def save_data(book, filename="addressbook.pkl"):
    pass

def load_data(filename="addressbook.pkl"):
    pass

def save_notes(notes_book, filename="notesbook.pkl"):
    pass

def load_notes(filename="notesbook.pkl"):
    pass
# -----------------------------------------------------------
# -----------------------------------------------------------окремий файл
# Декоратор для обробки помилок
def input_error(func):
    pass
# -------------------------------------------------------------
# -------------------------------------------------------------окремий файл
# Виведення доступних команд
def show_commands():
    pass
# ----------------------------------------------------------------
# -----------------------------------------------------------------окремий файл
# Основна функція для запуску програми оставити у файлі main.py
def main():
    pass

if __name__ == "__main__":
    main()
