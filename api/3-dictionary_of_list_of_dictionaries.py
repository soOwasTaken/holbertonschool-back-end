#!/usr/bin/python3
"""Gather data from an API"""

import json
import requests

USERS_URL = "https://jsonplaceholder.typicode.com/users?id="
TODOS_URL = "https://jsonplaceholder.typicode.com/todos"


def gather_todo_data():
    """Gather data about employees TODOs"""

    response = requests.get(TODOS_URL).json()
    todos_by_user = {}
    for todo in response:
        if todo['userId'] not in todos_by_user:
            todos_by_user[todo['userId']] = []
        todos_by_user[todo['userId']].append({
            'username': get_username(todo['userId']),
            'task': todo['title'],
            'completed': todo['completed']
        })

    with open('todo_all_employees.json', 'w') as f:
        json.dump(todos_by_user, f)


def get_username(user_id):
    """Fetch username for given user ID"""
    response = requests.get(USERS_URL + str(user_id)).json()
    return response[0]['username']
