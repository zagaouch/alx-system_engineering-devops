#!/usr/bin/python3

"""use api json"""
import requests
import sys

if __name__ == '__main__' :
    emp_id = sys.argv[1]
    api_url = 'https://jsonplaceholder.typicode.com'
    usr_uri = '{url}/users/{id}'.format(url=api_url, id=emp_id)
    todo_uri = '{url}/todos'.format(url=usr_uri)

    #user request
    res = requests.get(usr_uri).json()

    user_name = res.get('name')

    #todo request

    res =requests.get(todo_uri).json()
    tasks_number = len(res)
    task_non_complet = sum([task['completed'] is False for task in res])
    task_complelet = sum([task['completed'] is True for task in res])
    print(task_non_complet)
    print(task_complelet)
    str = "Employee {name} is done with tasks({tasknc}/{taskc}) : "
    print(str.format(name=user_name,tasknc=task_non_complet,taskc=task_complelet))
    for task in res :
        if task.get('completed') is True :
            print('\t',task.get('title'))


