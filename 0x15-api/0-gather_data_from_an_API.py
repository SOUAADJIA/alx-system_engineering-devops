#!/usr/bin/python3
"""Gather data from an API."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    user_ID = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(url, user_ID)
    data_url = "{}/todos?userId={}".format(url, user_ID)

    try:
        # Get user's info
        resp = requests.get(user_url)
        resp.raise_for_status()  # Raise an exception for HTTP errors
        user = resp.json()

        # Get user's todos
        resp = requests.get(data_url)
        resp.raise_for_status()  # Raise an exception for HTTP errors
        todos = resp.json()

        done = sum(1 for task in todos if task.get("completed"))
        total = len(todos)

        print("Employee {} is done with tasks({}/{}):".format(
            user.get("name"), done, total))

        for task in todos:
            if task.get("completed"):
                print("\t{}".format(task.get("title")))
    except requests.RequestException as e:
        print("Error fetching data:", e)
