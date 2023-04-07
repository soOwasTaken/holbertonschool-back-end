#!/usr/bin/python3
"""Json to ouput in python"""
import json
import requests

users_url = "https://jsonplaceholder.typicode.com/users?id="
todos_url = "https://jsonplaceholder.typicode.com/todos"


def gather_todo_data():
    """ Gather data about employee TODOs """

    response = requests.get(todos_url).json()
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
    """ Fetch username for given user ID """
    response = requests.get(users_url + str(user_id)).json()
    return response[0]['username']
