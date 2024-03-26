#!/usr/bin/python3
"""Gather data from an API and export to JSON."""

import json
import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{base_url}/users"
    todos_url = f"{base_url}/todos"

    users_resp = requests.get(users_url)
    users_data = users_resp.json()

    todos_resp = requests.get(todos_url)
    todos_data = todos_resp.json()

    user_tasks = {}

    for user in users_data:
        user_id = str(user["id"])
        username = user["username"]
        user_tasks[user_id] = []

        for task in todos_data:
            if str(task["userId"]) == user_id:
                task_data = {
                    "username": username,
                    "task": task["title"],
                    "completed": task["completed"]
                }
                user_tasks[user_id].append(task_data)

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(user_tasks, json_file, indent=4)
