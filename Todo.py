class Todo:
    def __init__(self, todo_id, title, completed):
        self.id = todo_id
        self.title = title
        self.completed = completed

    def __str__(self):
        return f'{self.id} | {self.title} | Completed: {self.completed}'

    def change_status(self, new_status):
        if type(new_status) is not bool:
            print('Status must be a boolean value (True or False).')
            return

        self.completed = new_status
        print('Todo status changed successfully.')
        print('------------------------------------------')
