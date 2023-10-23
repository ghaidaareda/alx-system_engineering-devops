#!/usr/bin/python3
"""
Python script that,
using  REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
from sys import argv


def get_employee_name(id):
    """get user name"""
    url = f'https://jsonplaceholder.typicode.com/users/{id}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        name = data['name']
        return name


def to_do_done(id):
    """check done tasks"""
    url = f'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        total = len(data)
        done = 0
        completed_tasks = []
        for item in data:
            if item['userId'] == id and item['completed']:
                done += 1
                completed_tasks.append(item['title'])
        employee_name = get_employee_name(id)
        print(f'Employee {employee_name} is done with tasks ({done}/{total})')
        for task in completed_tasks:
            print(f'\t {task}')


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        id = int(sys.argv[1])
        to_do_done(id)
