#!/usr/bin/python3
"""
extend Python script to export data in the json format
for all empolyee
"""
if __name__ == '__main__':
    import json
    import requests
    import sys

    url_1 = f'https://jsonplaceholder.typicode.com/users'
    url_2 = f'https://jsonplaceholder.typicode.com/todos'
    response_1 = requests.get(url_1)
    response_2 = requests.get(url_2)

    data_1 = response_1.json()
    data_2 = response_2.json()
    tasks = []
    for user in data_1:
        user_tasks = []
        for item in data_2:
            if item['userId'] == user['id']:
                task = {"task": item['title'],
                        "completed": item['completed'],
                        "username": user['username']
                        }
            user_tasks.append(task)   
        user_tasks_dict = {user['id']: user_tasks}
        tasks.append(user_tasks_dict)
    with open('todo_all_employees.json', 'w') as file:
        json.dump(tasks, file)
