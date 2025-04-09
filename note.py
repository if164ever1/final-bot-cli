from datetime import datetime
from collections import UserDict

class Note:
    def __init__(self, text, tags=None):
        self.text = text
        self.created = datetime.now()
        self.tags = tags if tags else []
    
    def edit(self, new_text):
        self.text = new_text
        self.created = datetime.now()
    
    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)
    
    def __str__(self):
        tag_str = f" [Tags: {', '.join(self.tags)}]" if self.tags else ""
        return f"{self.text}{tag_str} (Created: {self.created.strftime('%d.%m.%Y %H:%M')})"