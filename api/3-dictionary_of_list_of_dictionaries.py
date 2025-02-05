#!/usr/bin/python3
# Author: Joana Casallas
"""REST API - getter data"""
import json
import requests
import sys


try:
    url_users = "https://jsonplaceholder.typicode.com/users"
    r_users = requests.get(url_users)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

users = r_users.json()

userId = ""
data = {}

for user in users:
    userId = user['id']

    url_todo = f"https://jsonplaceholder.typicode.com/todos?userId={userId}"
    r_todo = requests.get(url_todo)
    if r_todo.status_code != 200 or not r_todo.json():
        print(f"Error: Failed to fetch tasks for userId {userId}")
        sys.exit(1)

    todo = r_todo.json()
    tasks = []
    for task in todo:
        tasks.append({
            'username': user['username'],
            'task': task['title'],
            'completed': task['completed']
            })
    data[userId] = tasks

json_filename = "todo_all_employees.json"

with open(json_filename, mode="w", encoding="utf-8") as file:
    json.dump(data, file)
