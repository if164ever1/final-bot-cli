import unittest
from datetime import datetime, timedelta
from main import AddressBook, Record, Name, Birthday  # імпортуй з main.py

class TestAddressBook(unittest.TestCase):
    def test_get_upcoming_birthdays(self):
        book = AddressBook()

        # Сьогоднішня дата
        today = datetime.today().date()

        # Створимо 2 записи: один із ДН через 3 дні, інший через 10
        record1 = Record(Name("Оля"))
        record1.add_birthday(Birthday((today + timedelta(days=3)).strftime("%d.%m.%Y")))
        book.add_record(record1)

        record2 = Record(Name("Петро"))
        record2.add_birthday(Birthday((today + timedelta(days=10)).strftime("%d.%m.%Y")))
        book.add_record(record2)

        result = book.get_upcoming_birthdays(days=7)
        self.assertIn(record1, result)
        self.assertNotIn(record2, result)

if __name__ == '__main__':
    unittest.main()