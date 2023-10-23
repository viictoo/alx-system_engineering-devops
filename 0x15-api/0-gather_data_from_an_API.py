#!/usr/bin/python3
"""a Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress
"""
import requests
from sys import argv as av


def getData():
    """get and display required data
    """
    id = av[1]
    uri = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(id)
    resp = requests.get(uri).json()

    uri = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    employee = (requests.get(uri).json())
    name = employee.get("name")

    tasks = []
    total, completed = 0, 0
    for task in resp:
        total += 1
        if task.get("completed") is True:
            tasks.append(task.get("title"))
            completed += 1

    print("Employee {} is done with tasks({}/{}):".format(name, completed,
                                                          total))
    for tsk in tasks:
        print('\t {}'.format(tsk))


if __name__ == "__main__":
    getData()
