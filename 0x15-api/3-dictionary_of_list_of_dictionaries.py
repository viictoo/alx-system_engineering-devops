#!/usr/bin/python3
"""api module"""
import json
import requests
from sys import argv as av


def getName():
    """
    get employee name from id
    """
    uri = 'https://jsonplaceholder.typicode.com/users/'

    response = requests.get(uri)
    employees = (response.json())
    if employees:
        listAll = []
        for emp in employees:
            lis = [f"{emp.get('id')}", emp.get("username")]
            listAll.append(lis)
        return (listAll)
    else:
        print("Not a Valid JSON")
        exit(-1)


def getAllData(employees):
    """get and display required data
    """

    uri = 'https://jsonplaceholder.typicode.com/todos/'

    response = requests.get(uri)
    resp = (response.json())
    # print(resp)
    if resp:
        try:
            row = []
            dic, jDic = {}, {}
            for employee in employees:
                for task in resp:
                    if int(employee[0]) == task.get("userId"):
                        dic["task"] = task.get("title")
                        dic["completed"] = task.get("completed")
                        dic["username"] = employee[1]
                        row.append(dic)

                jDic[employee[0]] = row

            filename = "todo_all_employees.json"

            with open(filename, 'w') as file:
                json.dump(jDic, file)

        except Exception as e:
            print("Some exception occured", e)
            return (-1)
    else:
        print("Not a Valid JSON")
        exit(-1)


if __name__ == "__main__":

    employees = getName()
    getAllData(employees)
