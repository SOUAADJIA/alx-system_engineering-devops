#!/usr/bin/python3
"""Gather data from an API and write to CSV."""
import requests
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
    with open(employee_id + ".csv", "w") as file:
        for task in todos:
            file.write("\"{}\",\"{}\",\"{}\",\"{}\"\n".format(
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ))
