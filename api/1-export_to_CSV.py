#!/usr/bin/python3
"""Json to output in python"""

import csv
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
    completed_tasks = []
    for task_list in task_lists:
        if task_list["completed"]:
            completed_tasks.append(task_list)

    employee_name = name_scrapping[0]['username']
    file_name = f"{employee_id}.csv"

    with open(file_name, mode='w') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME',
                      'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for task in completed_tasks:
            writer.writerow({'USER_ID': employee_id, 'USERNAME': employee_name,
                             'TASK_COMPLETED_STATUS': str(task["completed"]), 'TASK_TITLE': task["title"]})
    print(f"Task data for employee {employee_name} saved to {file_name}")
