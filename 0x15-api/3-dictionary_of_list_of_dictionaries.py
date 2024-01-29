#!/usr/bin/python3
"""
Python script that, using  REST API,
for a given employee ID,
returns information about
his/her TODO list progress
"""


if __name__ == "__main__":
    import json
    import requests
    import sys

    url_1 = f"https://jsonplaceholder.typicode.com/users"
    url_2 = "https://jsonplaceholder.typicode.com/todos"

    p = requests.get(url_1)
    content = json.loads(p.content)
    r = requests.get(url_2)
    content_2 = json.loads(r.content)

    main = {}
    dct = {}
    sub = {}
    ls = []
    id = 0
    for usr in content:
        id += 1
        ls = []
        for item in content_2:
            if item["userId"] == id:
                sub = {}
                sub["username"] = content[id - 1]["username"]
                sub["task"] = item["title"]
                sub["completed"] = item["completed"]
                ls.append(sub)
        dct[id] = ls

    with open("todo_all_employees.json", "w") as fd:
        json.dump(dct, fd)
