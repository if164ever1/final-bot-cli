from colorama import Fore, Style, init
from assistant.address_book import AddressBook
from assistant.notesbook import NotesBook
from assistant.serialization import save_data, load_data
from assistant.parser import parse_command, execute_command  # тобто з parser.py
from colorama import Fore, Style, init

init(autoreset=True) # Автоматичне скидання кольору після Fore.RED

# Завантаження існуючих даних або створення нових
try:
    contacts, notes = load_data()
except Exception as e:
    print(Fore.RED + f"Error loading data: {e}")
    contacts = AddressBook()
    notes = NotesBook()


# Декоратор для обробки помилок
def input_error(func):
    pass

# Функція для обробки команд
def parse_input():
    pass

def main():
    print(Fore.GREEN + "👋 Welcome to your Personal Assistant CLI!")
    print("Type 'exit', 'quit' or 'close' to stop.\n")
    while True:
        user_input = input(Fore.CYAN + ">>> " + Style.RESET_ALL)
        if user_input.lower() in ['exit', 'quit', 'close']:
            save_data(contacts, notes)
            print(Fore.GREEN + "👋 Bye! All data saved.")
            break
        
        command, arguments = parse_command(user_input)
        try:
            execute_command(command, arguments, contacts, notes)
        except Exception as e:
            print(Fore.RED + f"Error: {e}")
    

if __name__ == "__main__":
    main()