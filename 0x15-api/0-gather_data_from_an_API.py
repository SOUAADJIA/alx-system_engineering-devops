#!/usr/bin/python3
"""
Module Docs
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    url_str = 'https://jsonplaceholder.typicode.com/'
    user_str = '{}users/{}'.format(url_str, employee_id)
    todos_str = '{}todos?userId={}'.format(url_str, employee_id)
    employee_str = "Employee {} is done with tasks"

    try:
        res = requests.get(user_str)
        user_data = res.json()
        employee_name = user_data.get('name')

        res = requests.get(todos_str)
        tasks = [task for task in res.json() if task.get('completed')]

        print(employee_str.format(employee_name), end="")
        print("({}/{}):".format(len(tasks), len(res.json())))
        for task in tasks:
            print("\t{}".format(task.get("title")))
    except requests.RequestException as e:
        print("Error fetching data:", e)

