#!/usr/bin/python3
"""
Python script that, using  REST API,
for a given employee ID,
returns information about
his/her TODO list progress
"""


if __name__ == "__main__":
    import json
    import numpy as np
    import requests
    import sys

    if __name__ == "__main__":
        id = sys.argv[1]

        url_1 = f"https://jsonplaceholder.typicode.com/users/{id}"

        url_2 = "https://jsonplaceholder.typicode.com/todos"

        p = requests.get(url_1)
        content = json.loads(p.content)
        name = content["name"]

        r = requests.get(url_2)
        content_2 = json.loads(r.content)

        alist = []

        for item in content_2:
            if item["userId"] == int(id):
                temp = '"{}", "{}", "{}", "{}"'.format(
                    id, name, item["completed"], item["title"]
                )
                alist.append(temp)

        arr = np.array(alist)
        np.savetxt(f"{id}.csv", arr, fmt="%s")
