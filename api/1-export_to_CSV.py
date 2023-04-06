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

    employee_name = name_scrapping[0]['username']
    file_name = f"{employee_id}.csv"

    with open(file_name, mode='w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for i, task in enumerate(task_lists, start=1):
            writer.writerow([f"{employee_id}", f"{employee_name}",
                             f"{task['completed']}", f"{task['title']}"])
    print(f"Task data for employee {employee_name} saved to {file_name}")
