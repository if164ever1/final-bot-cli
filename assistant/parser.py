# Парсер команд
def parse_command(user_input):
    parts = user_input.strip().split()
    command = parts[0].lower()
    arguments = parts[1:]
    return command, arguments

# Виконання команд
def execute_command(command, arguments, book, notes_manager):
    if command == "add":
        if "contact" in arguments:
            name = arguments[1]
            phone = arguments[2]
            book.add_record(Record(name))
            print(f"Contact {name} added with phone {phone}")
        elif "note" in arguments:
            text = ' '.join(arguments[1:])
            notes_manager.add_note(text)
            print(f"Note added: {text}")
    
    elif command == "delete":
        if "contact" in arguments:
            name = arguments[1]
            book.delete(name)
            print(f"Contact {name} deleted.")
    
    elif command == "show":
        if "contacts" in arguments:
            for record in book.data.values():
                print(record)
    
    elif command == "birthday":
        upcoming = book.get_upcoming_birthdays()
        for name, date in upcoming:
            print(f"Upcoming birthday: {name} on {date}")
    
    elif command == "note":
        if "find" in arguments:
            tag = arguments[2] if len(arguments) > 2 else None
            notes = notes_manager.find_notes_by_tag(tag)
            for note in notes:
                print(note)
        elif "sort" in arguments:
            sorted_notes = notes_manager.sort_notes_by_tag()
            for note in sorted_notes:
                print(note)

if __name__ == "__main__":
    book = AddressBook()
    notes_manager = NotesManager()

    while True:
        user_input = input("Enter command: ")
        command, arguments = parse_command(user_input)
        execute_command(command, arguments, book, notes_manager)