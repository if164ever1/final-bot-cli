from collections import UserDict
from datetime import datetime
import pickle
import re

# Валідація


def validate_phone(phone):
    pattern = r"^\+?\d{10,15}$"
    return bool(re.match(pattern, phone))


def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    return bool(re.match(pattern, email))

# Класи для управління контактами


class Field:
    pass


class Name(Field):
    def __init__(self, name):
        self.name = name


class Phone(Field):
    def __init__(self, phone):
        if not validate_phone(phone):
            raise ValueError("Invalid phone number format.")
        self.phone = phone


class Email(Field):
    def __init__(self, email):
        if not validate_email(email):
            raise ValueError("Invalid email format.")
        self.email = email


class Address(Field):
    def __init__(self, address):
        self.address = address


class Birthday(Field):
    def __init__(self, birthday):
        self.birthday = datetime.strptime(birthday, '%Y-%m-%d')


class Record:
    def __init__(self, name, phone=None, email=None, address=None, birthday=None):
        self.name = name
        self.phones = [phone] if phone else []
        self.email = email
        self.address = address
        self.birthday = birthday

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.phone != phone.phone]

    def edit_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def edit_email(self, email):
        self.email = email

    def edit_address(self, address):
        self.address = address

    def days_to_birthday(self):
        if not self.birthday:
            return None
        today = datetime.today()
        next_birthday = self.birthday.birthday.replace(year=today.year)
        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year + 1)
        return (next_birthday - today).days


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.name] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self, days=7):
        today = datetime.today()
        upcoming = {}
        for record in self.data.values():
            if record.birthday:
                next_birthday = record.birthday.birthday.replace(
                    year=today.year)
                if next_birthday < today:
                    next_birthday = next_birthday.replace(year=today.year + 1)
                if (next_birthday - today).days <= days:
                    upcoming[record.name.name] = (next_birthday - today).days
        return upcoming

# Класи для управління нотатками


class Note:
    def __init__(self, content):
        self.content = content


class NotesBook(UserDict):
    def add_note(self, note_id, content):
        self.data[note_id] = Note(content)

    def delete_note(self, note_id):
        if note_id in self.data:
            del self.data[note_id]

    def edit_note(self, note_id, new_content):
        if note_id in self.data:
            self.data[note_id].content = new_content

    def search_notes(self, query):
        return {note_id: note for note_id, note in self.data.items() if query.lower() in note.content.lower()}

# Серіалізація та десеріалізація


def save_data(obj, filename):
    with open(filename, "wb") as file:
        pickle.dump(obj, file)


def load_data(filename):
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return None

# Основна функція


def main():
    address_book = load_data("addressbook.pkl") or AddressBook()
    notes_book = load_data("notesbook.pkl") or NotesBook()

    print("Welcome to Personal Assistant!")
    print("\nAvailable commands:")
    print("1. add_contact - Add a new contact")
    print("2. show_contacts - Show all contacts")
    print("3. find_contact - Find a contact by name")
    print("4. delete_contact - Delete a contact by name")
    print("5. edit_contact - Edit a contact")
    print("6. birthdays - Show upcoming birthdays within given days")
    print("7. add_note - Add a new note")
    print("8. show_notes - Show all notes")
    print("9. search_notes - Search notes")
    print("10. edit_note - Edit a note")
    print("11. delete_note - Delete a note")
    print("12. exit - Save data and exit\n")

    while True:
        command = input("Enter command: ").strip().lower()
        if command == "add_contact":
            try:
                name = input("Enter name: ")
                phone = input("Enter phone: ")
                email = input("Enter email (optional): ") or None
                address = input("Enter address (optional): ") or None
                birthday = input(
                    "Enter birthday (YYYY-MM-DD, optional): ") or None
                record = Record(Name(name), Phone(phone),
                                Email(email) if email else None,
                                Address(address) if address else None,
                                Birthday(birthday) if birthday else None)
                address_book.add_record(record)
                print(f"Contact {name} added.")
            except ValueError as e:
                print(e)
        elif command == "show_contacts":
            for name, record in address_book.items():
                phones = ", ".join([p.phone for p in record.phones])
                print(f"Name: {name}, Phones: {phones}, "
                      f"Email: {record.email.email if record.email else 'N/A'}, "
                      f"Address: {record.address.address if record.address else 'N/A'}, "
                      f"Birthday: {record.birthday.birthday.strftime('%Y-%m-%d') if record.birthday else 'N/A'}")
        elif command == "find_contact":
            name = input("Enter name to find: ")
            record = address_book.find(name)
            if record:
                phones = ", ".join([p.phone for p in record.phones])
                print(f"Name: {record.name.name}, Phones: {phones}, "
                      f"Email: {record.email.email if record.email else 'N/A'}, "
                      f"Address: {record.address.address if record.address else 'N/A'}, "
                      f"Birthday: {record.birthday.birthday.strftime('%Y-%m-%d') if record.birthday else 'N/A'}")
            else:
                print(f"No contact found with name {name}.")
        elif command == "delete_contact":
            name = input("Enter name to delete: ")
            address_book.delete(name)
            print(f"Contact {name} deleted.")
        elif command == "edit_contact":
            name = input("Enter name to edit: ")
            record = address_book.find(name)
            if record:
                email = input("Enter new email (optional): ") or record.email
                address = input(
                    "Enter new address (optional): ") or record.address
                record.edit_email(Email(email) if email else None)
                record.edit_address(Address(address) if address else None)
                print(f"Contact {name} updated.")
            else:
                print(f"No contact found with name {name}.")
        elif command == "birthdays":
            days = int(input("Enter number of days: "))
            upcoming = address_book.get_upcoming_birthdays(days)
            for name, days_left in upcoming.items():
                print(f"{name}: in {days_left} days")
        elif command == "add_note":
            note_id = input("Enter note ID: ")
            content = input("Enter note content: ")
            notes_book.add_note(note_id, content)
            print(f"Note {note_id} added.")
        elif command == "show_notes":
            for note_id, note in notes_book.items():
                print(f"Note ID: {note_id}, Content: {note.content}")
        elif command == "search_notes":
            query = input("Enter search query: ")
            results = notes_book.search_notes(query)
            for note_id, note in results.items():
                print(f"Note ID: {note_id}, Content: {note.content}")
        elif command == "edit_note":
            note_id = input("Enter note ID to edit: ")
            new_content = input("Enter new content: ")
            notes_book.edit_note(note_id, new_content)
            print(f"Note {note_id} updated.")
        elif command == "delete_note":
            note_id = input("Enter note ID to delete: ")
            notes_book.delete_note(note_id)
            print(f"Note {note_id} deleted.")
        elif command == "exit":
            save_data(address_book, "addressbook.pkl")
            save_data(notes_book, "notesbook.pkl")
            print("Data saved. Goodbye!")
            break
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
