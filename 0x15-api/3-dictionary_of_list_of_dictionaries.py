#!/usr/bin/python3
"""
contains a python script that, using the JSONplaceholder API, for a given
employee ID, returns all tasks from all employees, in JSON format
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    '''Gives name of employee and completed tasks and exports as JSON file
    for all users
    '''
    url = "https://jsonplaceholder.typicode.com/users"
    req = requests.get(url)
    jreq = req.json()
    id_dict = {}
    id_name = {}

    for i in jreq:
        id_dict.update({i['id']: []})
        id_name.update({i['id']: i['username']})
    url = "https://jsonplaceholder.typicode.com/todos"
    req = requests.get(url)
    jreq = req.json()
    tasks = []
    tasks_dict = []
    for k in id_dict.keys():
        for i in jreq:

            if k == i['userId']:
                tasks_dict.append({'task': i['title'],
                                   'completed': i['completed'],
                                   'username': id_name[k]})
                continue
        id_dict.update({k: tasks_dict})
        tasks_dict = []
    with open('todo_all_employees.json', mode='w') as json_file:
        json.dump(id_dict, json_file)
