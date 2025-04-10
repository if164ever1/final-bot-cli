from .record import Record


# Парсер команд
def parse_command(user_input:str):
    parts = user_input.strip().split()
    if not parts:
        return "", []
    command = parts[0].lower()
    arguments = parts[1:]
    return command, arguments

# Виконання команд
def execute_command(command:str, arguments:list, book, notes_manager):
    if command == "add":
        if arguments and arguments[0] == "contact":
            if len(arguments) < 3:
                print("❗ Please provide both name and phone.")
                return
            name = arguments[1]
            phone = arguments[2]
            record = Record(name)
            record.add_phone(phone)
            book.add_record(Record(record))
            print(f"✅ Contact '{name}' added with phone {phone}")
        elif arguments and arguments[0] == "note":
            text = ' '.join(arguments[1:])
            if not text:
                print("❗ Cannot add empty note.")
                return
            notes_manager.add_note(text)
            print(f"📝 Note added: {text}")
    
    elif command == "delete":
        if arguments and arguments[0] == "contact":
            if len(arguments) < 2:
                print("❗ Please provide the contact name to delete.")
                return
            name = arguments[1]
            try:
                book.delete(name)
                print(f"🗑️ Contact '{name}' deleted.")
            except KeyError:
                print(f"❌ Contact '{name}' not found.")
    
    elif command == "show":
        if arguments and arguments[0] == "contacts":
            if not book.data:
                print("ℹ️ No contacts available.")
                return
            for record in book.data.values():
                print(record)
    
    elif command == "birthday":
        upcoming = book.get_upcoming_birthdays()
        if not upcoming:
            print("🎉 No upcoming birthdays.")
        else:
            for record in upcoming:
                print(f"🎉 Upcoming birthday: {record.name.value} on {record.birthday}")
    
    elif command == "note":
        if len(arguments) < 2:
            print("❗ Usage: 'note find <tag>' or 'note sort'")
            return
        
        if "find" in arguments:
            tag = arguments[2] if len(arguments) > 2 else None
            notes = notes_manager.find_notes_by_tag(tag)
            if notes:
                for note in notes:
                    print(note)
            else:
                print(f"🔍 No notes found with tag '{tag}'.")
        elif "sort" in arguments:
            sorted_notes = notes_manager.sort_notes_by_tag()
            if sorted_notes:
                for note in sorted_notes:
                    print(note)
            else:
                print("ℹ️ No notes to sort.")