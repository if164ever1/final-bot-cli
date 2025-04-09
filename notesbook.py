from collections import UserDict
from note import Note

class NotesBook(UserDict):
    def add_note(self, text, tags=None):
        note = Note(text, tags)
        note_id = str(len(self.data) + 1)
        self.data[note_id] = note
    
    def delete_note(self, note_id):
        if note_id in self.data:
            del self.data[note_id]
        else:
            raise KeyError(f"Note with ID {note_id} not found.")
    
    def edit_note(self, note_id, new_text):
        if note_id in self.data:
            self.data[note_id].edit(new_text)
        else:
            raise KeyError(f"Note with ID {note_id} not found.")
    
    def find_notes_by_tag(self, tag):
        return [note for note in self.data.values() if tag in note.tags]

    def sort_notes_by_tag(self):
        return sorted(self.data.values(), key=lambda note: note.tags)

    def __str__(self):
        return "\n".join(f"[{note_id}] {note}" for note_id, note in self.data.items())