import streamlit as st
from todo_functions import *

todos_list = load_todos()

def complete_todo():
    for todo in todos_list:
        if st.session_state[todo] == True:
            todos_list.remove(todo)
        update_todos(todos_list)


def add_todo():
    new_todo = st.session_state["new_todo"]
    todos_list.append(new_todo)
    update_todos(todos_list)

st.title("My ToDo List")
st.write("\n\n")

for todo in todos_list:
    st.checkbox(label=todo, key=todo, on_change=complete_todo)

st.text_input(label="", placeholder="Enter a new todo", key="new_todo", on_change=add_todo)