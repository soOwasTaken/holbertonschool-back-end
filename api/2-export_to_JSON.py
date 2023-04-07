#!/usr/bin/python3
"""Json to ouput in python"""
import requests
import sys
import json

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
    completed_tasks = []
    for task_list in task_lists:
        if task_list["completed"]:
            completed_tasks.append({
                "task": task_list["title"],
                "completed": task_list["completed"],
                "username": name_scrapping[0]['name']
            })

    employee_name = name_scrapping[0]['name']
    total_tasks = len(task_lists)
    num_completed_tasks = len(completed_tasks)

    print(
        f"Employee {employee_name} is done with tasks\
({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['task']}")

    # Exporting data in JSON format
    with open(f"{employee_id}.json", "w") as f:
        json.dump({employee_id: completed_tasks}, f)
