#!/usr/bin/python3
"""
Extend Python script to export data in the
JSON format for all employees' tasks.
"""
import json
import requests

if __name__ == '__main__':
    url_users = 'https://jsonplaceholder.typicode.com/users'
    url_todos = 'https://jsonplaceholder.typicode.com/todos'

    response_users = requests.get(url_users)
    response_todos = requests.get(url_todos)

    users = response_users.json()
    todos = response_todos.json()

    user_tasks = {}
    for user in users:
        user_id = user['id']
        username = user['username']
        user_tasks[user_id] = []

        for todo in todos:
            if todo['userId'] == user_id:
                task = {
                    "username": username,
                    "task": todo['title'],
                    "completed": todo['completed']
                }
                user_tasks[user_id].append(task)

    with open('todo_all_employees.json', 'w') as file:
        json.dump(user_tasks, file)
