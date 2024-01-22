from Todo import Todo


def display_actions():
    print('1. List all todos')
    print('2. Add a new todo')
    print('3. Change a todo status')
    print('4. Delete a todo')
    print('5. Exit')
    print('What would you like to do ?')


def display_todos(todos):
    print('---------- Here are all your todos ----------')
    for todo in todos:
        print(todo)
    print('--------------------------------------------')


def add_todo(todos):
    print('---------- Add a new todo (enter q to quit) ----------')
    title = input('Title: ')
    if title == 'q':
        return
    todo_id = len(todos) + 1
    todo = Todo(todo_id, title, False)
    todos.append(todo)
    print('Todo added successfully.')
    print('----------------------------------')


def change_todo_status(todos):
    print('---------- Change a todo status ----------')
    todo_id = input('Todo ID (enter q to quit): ')
    while not todo_id.isdigit():
        if todo_id == 'q':
            return
        print('Please enter a valid ID.')
        todo_id = input('Todo ID: ')
    todo_id = int(todo_id)
    for todo in todos:
        if todo.id == todo_id:
            print(f'Current status: {todo.completed}')
            todo.change_status()
            print('Todo status changed successfully.')
            print('----------------------------------')
        else:
            print("No todo found with this id")


def delete_todo(todos):
    print('---------- Delete a todo ----------')
    todo_id = input('Todo ID: (enter q to quit) ')
    if todo_id == 'q':
        return
    while not todo_id.isdigit():
        print('Please enter a valid ID.')
        todo_id = (input('Todo ID: '))
    todo_id = int(todo_id)
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            print('Todo deleted successfully.')
            print('----------------------------------')
        else:
            print("No todo found with this id")


def check_action(action):
    while action not in ['1', '2', '3', '4', '5']:
        print('Please enter a valid action.')
        action = input('')
