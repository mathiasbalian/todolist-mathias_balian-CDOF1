class Todo:
    def __init__(self, todo_id, title, completed):
        self.id = todo_id
        self.title = title
        self.completed = completed

    def __str__(self):
        return f'{self.id} | {self.title} | Completed: {self.completed}'

    def change_status(self):
        self.completed = not self.completed
        print('Todo status changed successfully.')
        print('------------------------------------------')
