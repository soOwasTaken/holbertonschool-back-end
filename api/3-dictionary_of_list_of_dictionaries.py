#!/usr/bin/python3
"""Json to ouput in python"""
import json
import requests
import sys

if __name__ == "__main__":
    # retrieve all employee IDs from the API
    response_users = requests.get(
        "https://jsonplaceholder.typicode.com/users")
    users = response_users.json()

    # loop through all employee IDs and retrieve tasks for each employee
    all_tasks = {}
    for user in users:
        response = requests.get(
            f"https://jsonplaceholder.typicode.com/todos?userId={user['id']}")
        task_lists = response.json()
        tasks = []
        for task_list in task_lists:
            task = {
                "username": user['username'],
                "task": f"{user['username']} - {task_list['title']}",
                "completed": task_list["completed"]
            }
            tasks.append(task)
        all_tasks[user['id']] = tasks

    # create the output dictionary with all tasks
    output_dict = all_tasks

    with open("todo_all_employees.json", "w") as outfile:
        json.dump(output_dict, outfile)
