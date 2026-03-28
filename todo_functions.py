def load_todos():
    with open("todos.txt") as f:
        todos_list = f.readlines()
        todos_list = [todo[:-1] for todo in todos_list]
    return todos_list

def update_todos(todos_list):
    with open("todos.txt","w") as f:
        f.writelines([todo+"\n" for todo in todos_list])

