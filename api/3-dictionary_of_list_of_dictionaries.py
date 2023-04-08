#!/usr/bin/python3
"""Gather data from an API"""

import json
import requests

if __name__ == '__main__':
    API = 'https://jsonplaceholder.typicode.com'
    user_response = requests.get(f"{API}/users/").json()
    tlist_response = requests.get(f"{API}/todos").json()
    task_by_user = {}
    for task in tlist_response:
        user_id = task['userId']
        if user_id not in task_by_user:
            task_by_user[user_id] = []
        task_by_user[user_id].append({
            "task": task['title'],
            "completed": task['completed'],
            "username": next(user[
                'username'] for user in user_response if user['id'] == user_id)
        })

    with open("todo_all_employees.json", mode='w') as json_file:
        json.dump(task_by_user, json_file)
