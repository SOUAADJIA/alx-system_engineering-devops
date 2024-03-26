#!/usr/bin/python3
"""Gather data from an API and export to CSV."""
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

    csv_filename = "{}.csv".format(employee_id)
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = [
                "USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for task in todos:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": user_data.get("name"),
                "TASK_COMPLETED_STATUS": str(task.get("completed")),
                "TASK_TITLE": task.get("title")
            })
