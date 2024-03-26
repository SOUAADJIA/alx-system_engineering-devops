#!/usr/bin/python3
"""Gather data from an API and write to JSON."""
import requests
import json
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, employee_id)
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)

    user_resp = requests.get(user_url)
    user_data = user_resp.json()

    todos_resp = requests.get(todos_url)
    todos = todos_resp.json()

    username = user_data.get("username")

    user_tasks = []
    for task in todos:
        task_data = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        user_tasks.append(task_data)

    output_data = {employee_id: user_tasks}

    with open(employee_id + ".json", "w") as file:
        json.dump(output_data, file)
