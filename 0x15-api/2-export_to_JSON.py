#!/usr/bin/python3
"""
extend Python script to export data in the CSV format
"""
if __name__ == '__main__':
    import json
    import requests
    import sys

    url_1 = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}'
    url_2 = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos'
    response_1 = requests.get(url_1)
    response_2 = requests.get(url_2)

    data_1 = response_1.json()
    data_2 = response_2.json()
    tasks = []
    for item in data_2:
        task = {"task": item['title'],
                "completed": item['completed'],
                "username": data_1['username']
                }
        tasks.append(task)
    user_tasks = {data_1['id']: tasks}

    with open(f'{sys.argv[1]}.json', 'w') as file:
        json.dump(user_tasks, file)
