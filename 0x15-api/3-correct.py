#!/usr/bin/python3
"""
Gather data about employees TODO and export to JSON
"""
import json
import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users?id="
todos_url = "https://jsonplaceholder.typicode.com/todos"


def user_info():
    """ Fetch user info """

    from collections import defaultdict
    correct_output = defaultdict(list)

    response = requests.get(todos_url).json()
    for item in response:
        url = users_url + str(item['userId'])
        usr_resp = requests.get(url).json()

        correct_output[item['userId']].append(
            {'username': usr_resp[0]['username'],
            'completed': item['completed'],
            'task': item['title']})

    with open('todo_all_employees.json', 'w') as f:
        json.dump(correct_output, f)

if __name__ == "__main__":
    user_info()
