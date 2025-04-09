import pickle
from colorama import Fore, Style, init
from notesbook import NotesBook

init(autoreset=True)

# serialisation


def save_data(book, filename="addressbook.pkl"):
    try:
        with open(filename, "wb") as f:
            pickle.dump(book, f)
        print(f"{Fore.CYAN}Data saved successfully.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error saving data: {e}{Style.RESET_ALL}")


# deserialisation

def load_data():
    try:
        with open("addressbook.pkl", "rb") as f:
            return pickle.load(f)
    except (FileNotFoundError, EOFError):
        print(
            f"{Fore.YELLOW}No saved data found. Returning a new AddressBook.{Style.RESET_ALL}")
        return AddressBook()
    except Exception as e:
        print(f"{Fore.RED}Error loading data: {e}{Style.RESET_ALL}")
        return AddressBook()

# serialisation notes


def save_notes(notes_book, filename="notes.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(notes_book, f)
    print(f"{Fore.CYAN}Notes saved successfully.{Style.RESET_ALL}")


# deserialisation notes


def load_notes(filename="notes.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except (FileNotFoundError, EOFError):
        print(
            f"{Fore.YELLOW}No saved notes found. Returning a new NotesBook.{Style.RESET_ALL}")
        return NotesBook()
    except Exception as e:
        print(f"{Fore.RED}Error loading notes: {e}{Style.RESET_ALL}")
        return NotesBook()
