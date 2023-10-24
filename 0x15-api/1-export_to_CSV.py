#!/usr/bin/python3
"""
Python script that,
using  REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""
import csv
import requests
import sys

url_1 = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}'
url_2 = f'https://jsonplaceholder.typicode.com/user/{sys.argv[1]}/todos'
response_1 = requests.get(url_1)
response_2 = requests.get(url_2)

data_1 = response_1.json()
data_2 = response_2.json()

with open(f'{sys.argv[1]}.csv', 'w') as file:
    csv_writer = csv.writer(file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
    for item in data_2:
        csv_writer.writerow([data_1['id'], data_1['username'],
                             item['completed'], item['title']])
