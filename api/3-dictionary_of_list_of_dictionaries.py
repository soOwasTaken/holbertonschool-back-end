#!/usr/bin/python3
"""Json to output in python"""
import json
import requests

if __name__ == "__main__":
    # Get the list of all tasks
    response_tasks = requests.get("https://jsonplaceholder.typicode.com/todos")
    all_tasks = response_tasks.json()

    # Get the list of all users
    response_users = requests.get("https://jsonplaceholder.typicode.com/users")
    all_users = response_users.json()

    # Create a dictionary of tasks for each user
    user_tasks = {}
    for user in all_users:
        user_id = str(user["id"])
        username = user["name"]
        user_tasks[user_id] = []
        for task in all_tasks:
            if str(task["userId"]) == user_id:
                user_tasks[user_id].append(
                    {"username": username,
                     "task": task["title"],
                     "completed": task["completed"]})

    # Export the data to a JSON file
    filename = "todo_all_employees.json"
    with open(filename, "w") as f:
        json.dump(user_tasks, f)
