#!/usr/bin/python3
""" get request """
import json
import requests
import sys

def retrieve_todo_list_progress(emp_id):
    """ returns todolist progress given employee id"""
    todo_url = "https://jsonplaceholder.typicode.com"
    emp_url = f"{todo_url}/todos?userId={emp_id}"
    user_url = f"{todo_url}/users/{emp_id}"
    try:
        user_info = requests.get(user_url).json()
        user_name = user_info.get('name')

        todo_list = requests.get(emp_url).json()
        todo_size = len(todo_list)

        tasks_completed = []
        for todo in todo_list:
            if todo.get('completed') is True:
                tasks_completed.append(todo.get('title'))

        print("Employee {} is done with tasks({}/{}".format(
            user_name, len(tasks_completed), len(todo_list)))
        for todo in tasks_completed:
            print("\t {}".format(todo))
    except requests.exceptions.RequestException as int_rrror:
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    retrieve_todo_list_progress(int(sys.argv[1]))
