#!/usr/bin/python3
"""Gather data from an API and write to CSV."""
import csv
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

    completed_tasks = sum(1 for task in todos if task.get("completed"))

    print("Employee {} is done with tasks({}/{}):".format(
        user_data.get("name"), completed_tasks, len(todos)))

    csv_filename = "{}.csv".format(employee_id)
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ["ID", "NAME", "STATUS", "TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for task in todos:
            writer.writerow({
                "ID": employee_id,
                "NAME": user_data.get("name"),
                "STATUS": str(task.get("completed")),
                "TITLE": task.get("title")
            })

    print("Data exported to", csv_filename)
