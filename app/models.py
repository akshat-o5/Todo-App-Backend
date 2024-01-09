# models.py

class Todo:
    def __init__(self, title, completed=False, id=None):
        self.id = id
        self.title = title
        self.completed = completed

