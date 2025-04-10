# Personal Assistant CLI (final-bot-cli)

A command-line based personal assistant that helps you manage contacts and notes. Designed for structured organization, this assistant supports searching, editing, tagging, and birthday reminders — all from your terminal.

---

## 📌 Features

### 🧑‍🤝‍🧑 Contact Management
- Add, edit, delete contacts
- Store multiple phone numbers per contact
- Add birthdays with automatic upcoming birthday reminders
- Validate phone numbers and birthdates

### 📝 Notes Management
- Create, edit, delete text notes
- Tag notes with keywords
- Search notes by tag
- Sort notes by tag
- Store notes persistently

### 💾 Data Storage
- Automatically saves contacts and notes using `pickle`
- Data persists between program restarts
- Stored in local `/data` folder as `.bin` file

### 💻 CLI Interface
- Intuitive command parser
- Supports commands like: `add contact`, `add note`, `edit note`, `delete contact`, `note find tag`, etc.

---

## 📁 Project Structure ``` final-bot-cli/ ├── assistant/ # Core logic │ ├── address_book.py │ ├── contact_manager.py │ ├── note.py │ ├── notesbook.py │ ├── record.py │ ├── serialization.py │ └── __init__.py │ ├── cli/ # Command-line interface │ ├── main.py │ └── __init__.py │ ├── data/ # Saved data (pickle) │ └── data.bin │ ├── tests/ # Unit tests │ ├── test_addressbook.py │ ├── test_notes.py │ └── __init__.py │ ├── README.md # Project overview ├── requirements.txt # Dependencies └── .gitignore ```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Install dependencies:
```bash
pip install -r requirements.txt

cd cli
python main.py
