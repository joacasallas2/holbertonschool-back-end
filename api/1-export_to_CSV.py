#!/usr/bin/python3
# Author: Joana Casallas
"""REST API - getter data"""
import csv
import requests
import sys


if len(sys.argv) < 2:
    print("missing the User_id")
    sys.exit(1)

userId = sys.argv[1]

if not userId.isdigit():
    print("userId must be a number")
    sys.exit(1)

url_user = f"https://jsonplaceholder.typicode.com/users?id={userId}"
r_user = requests.get(url_user)
if r_user.status_code != 200 or not r_user.json():
    print(f"Error: userId {userId} not found")
    sys.exit(1)

user = r_user.json()
username = user[0]["username"]

url_todo = f"https://jsonplaceholder.typicode.com/todos?userId={userId}"
r_todo = requests.get(url_todo)
if r_todo.status_code != 200 or not r_todo.json():
    print(f"Error: Failed to fetch tasks for userId {userId}")
    sys.exit(1)

todo = r_todo.json()

csv_filename = f"{userId}.csv"

with open(csv_filename, mode="w", encoding="utf-8") as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    for task in todo:
        writer.writerow(
            [userId, username, task["completed"], task["title"]])
