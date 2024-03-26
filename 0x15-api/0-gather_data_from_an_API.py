#!/usr/bin/python3
"""Gather data from an API."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, employee_id)
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)

    user_resp = requests.get(user_url)
    user_data = user_resp.json()

    todos_resp = requests.get(todos_url)
    todos = todos_resp.json()

    completed_tasks = 0
    total_tasks = len(todos)

    for task in todos:
        if task.get("completed"):
            completed_tasks += 1

    print("Employee {} is done with tasks({}/{}):".format(
        user_data.get("name"), completed_tasks, total_tasks))

    for task in todos:
        if task.get("completed"):
            title = task.get("title")
            # Check formatting of task title
            if title.startswith('\t ') and title.endswith('\n'):
                print("\t{}: Format OK".format(title))
            else:
                print("\t{}: Incorrect Format".format(title))
