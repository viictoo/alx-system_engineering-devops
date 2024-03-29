#!/usr/bin/python3
"""api module"""
import json
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
        return (employee.get("username"))
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
            row = []
            jDic = {}
            for task in resp:
                dic = {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": name}
                row.append(dic)

            jDic[int(id)] = row
            # print(jDic)

            filename = "{}.json".format(id)

            with open(filename, 'w') as file:
                json.dump(jDic, file)

        except Exception as e:
            print("Some exception occured", e)
            return (-1)
    else:
        print("Not a Valid JSON")
        exit(-1)


if __name__ == "__main__":

    e_id = validator(av)
    name = getName(e_id)
    getData(e_id, name)
