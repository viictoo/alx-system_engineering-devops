#!/usr/bin/python3
"""api module"""
import requests
from sys import argv as av


def validator(av):
    """
    validate user input
    """
    if len(av) < 2:
        print("Usage: {} id".format(av[0]))
        exit(-1)
    try:
        int(av[1])
        return (av[1])
    except ValueError:
        print("id must be an integer")
        exit(-1)


def getName(id):
    """
    get employee name from id
    """
    uri = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)

    response = requests.get(uri)
    employee = (response.json())
    if employee:
        return (employee.get("name"))
    else:
        print("Not a Valid JSON")
        exit(-1)


def getData(id, name):
    """get and display required data
    """

    uri = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(id)

    response = requests.get(uri)
    resp = (response.json())
    if resp:
        try:
            tasks = []
            total, completed = 0, 0
            for task in resp:
                total += 1
                if task.get("completed") is True:
                    tasks.append(task.get("title"))
                    completed += 1

            print("Employee {} is done with tasks({}/{}):"
                  .format(name, completed, total))
            for tsk in tasks:
                print('\t {}'.format(tsk))

        except Exception:
            print("Some exception occured")
            return (-1)
    else:
        print("Not a Valid JSON")
        exit(-1)


if __name__ == "__main__":

    e_id = validator(av)
    name = getName(e_id)
    getData(e_id, name)
