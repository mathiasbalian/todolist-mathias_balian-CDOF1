from Tools import *
from Todo import Todo


todos = []
print("---------- Welcome to the Todo App! ----------")
while True:
    display_actions()
    action = input('')
    check_action(action)

    if action == '1':
        display_todos(todos)

    elif action == '2':
        add_todo(todos)

    elif action == '3':
        change_todo_status(todos)

    elif action == '4':
        delete_todo(todos)

    elif action == '5':
        print('---------- Thank you for using the Todo App! ----------')
        break
