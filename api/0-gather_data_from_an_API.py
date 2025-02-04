#!/usr/bin/python3
# Author: Joana Casallas
"""REST API - getter data"""
import requests
import sys

try:
    userId = sys.argv[1]
except Exception as e:
    print(f"error: {e}")

url_todo = f"https://jsonplaceholder.typicode.com/todos?userId={userId}"
url_user = f"https://jsonplaceholder.typicode.com/users?id={userId}"
r_todo = requests.get(url_todo)
r_user = requests.get(url_user)
todo = r_todo.json()
user = r_user.json()

employee_name = ""
completed_tasks = 0
total_tasks = 0
list_completed_tasks = []

for u in user:
    for k, v in u.items():
        if k == "name":
            employee_name = v
            break

for task in todo:
    total_tasks += 1
    for k, v in task.items():
        if k == "completed":
            if v is True:
                completed_tasks += 1
                list_completed_tasks.append(task['title'])

print(
    f"Employee {employee_name} is done with tasks"
    f"({completed_tasks}/{total_tasks}):"
    )
for task in list_completed_tasks:
    print(f"\t {task}")
