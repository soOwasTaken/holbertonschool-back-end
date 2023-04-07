#!/usr/bin/python3
"""Json to output in python"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("need employee_id")
        sys.exit(1)

    employee_id = sys.argv[1]
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    response_user_name = requests.get(
        f"https://jsonplaceholder.typicode.com/users?id={employee_id}")

    task_lists = response.json()
    name_scrapping = response_user_name.json()
    tasks = []
    for task_list in task_lists:
        task = {
            "task": task_list["title"],
            "completed": task_list["completed"],
            "username": name_scrapping[0]['username']
        }
        tasks.append(task)

    with open(f"{employee_id}.json", "w") as outfile:
        json.dump({employee_id: tasks}, outfile)
