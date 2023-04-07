#!/usr/bin/python3
"""Json to output in python"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Need employee_id")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Get the list of tasks for the given employee ID
    response_tasks = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    tasks = response_tasks.json()

    # Get the name of the employee
    response_name = requests.get(f"https://jsonplaceholder.typicode.com/users?id={employee_id}")
    employee_name = response_name.json()[0]['name']

    # Create a list of tasks for the employee
    task_list = []
    for task in tasks:
        task_list.append({"task": task["title"], "completed": task["completed"], "username": employee_name})

    # Print the tasks
    print(f"Tasks for employee {employee_name} ({len(task_list)} total):")
    for task in task_list:
        print(f"\t{task['task']} - {'Done' if task['completed'] else 'Not done'}")

    # Export the data to a JSON file
    filename = f"{employee_id}.json"
    with open(filename, "w") as f:
        json.dump({employee_id: task_list}, f)

    print(f"The data has been exported to {filename}")
