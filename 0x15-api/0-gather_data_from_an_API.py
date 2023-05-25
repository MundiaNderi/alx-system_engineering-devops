#!/usr/bin/python3
# Module that calls RESTful API

import requests
from sys import argv


if __name__ == "__main__":
    '''
    This module calls a RESTful API to retrieve employee information and their completed tasks.
    Usage: python module_name.py employee_id
    '''

    if len(argv) is not 2:
        print("Command takes 2 arguments")
        exit

    _id = argv[1]

    # Retrieve employee information
    employee_url = "https://jsonplaceholder.typicode.com/users/{}".format(_id)
    employee_req = requests.get(employee_url)
    employee_data = employee_req.json()
    name = employee_data['name']

    # Retrieve tasks information
    tasks_url = "https://jsonplaceholder.typicode.com/todos"
    tasks_req = requests.get(tasks_url)
    tasks_data = tasks_req.json()

    tasks = []
    completed_tasks = []

    # Filter tasks for the given employee ID
    for task in tasks_data:
        if task['userId'] == int(_id):
            tasks.append(task)

    total_tasks = len(tasks)

    # Filter completed tasks
    for task in tasks:
        if task['completed'] is True:
            completed_tasks.append(task)

    # Print employee's name and completed tasks
    print("Employee {} is done with tasks({}/{}):".format(name, len(completed_tasks), total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task['title']))
