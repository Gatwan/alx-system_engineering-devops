#!/usr/bin/python3
""" Script that gathers data from an API """
from requests import get
from sys import argv


def main():
    total_tasks = 0
    completed_tasks = 0
    task_res = get("https://jsonplaceholder.typicode.com/todos")
    user_res = get(
        "https://jsonplaceholder.typicode.com/users/{}".format(argv[1]))
    employee_name = user_res.json().get("name")

    for task in task_res.json():
        if task.get("userId") == int(argv[1]):
            if task.get("completed"):
                completed_tasks += 1
            total_tasks += 1

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, completed_tasks, total_tasks))

    for task in task_res.json():
        if task.get("userId") == int(argv[1]):
            if task.get("completed"):
                print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    main()
