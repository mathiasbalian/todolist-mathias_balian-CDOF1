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
    print('---------- Add a new todo ----------')
    title = input('Title: ')
    todo_id = len(todos) + 1
    todo = Todo(todo_id, title, False)
    todos.append(todo)
    print('Todo added successfully.')
    print('----------------------------------')


def change_todo_status(todos):
    print('---------- Change a todo status ----------')
    todo_id = input('Todo ID: ')
    todo = todos[int(todo_id) - 1]
    print(f'Current status: {todo.completed}')
    new_status = input('New status (True or False): ')
    todo.change_status(new_status)
    print('Todo status changed successfully.')
    print('------------------------------------------')


def delete_todo(todos):
    print('---------- Delete a todo ----------')
    todo_id = input('Todo ID: ')
    todo = todos[int(todo_id) - 1]
    todos.remove(todo)
    print('Todo deleted successfully.')
    print('----------------------------------')


def check_action(action):
    while action not in ['1', '2', '3', '4']:
        print('Please enter a valid action.')




