#!/usr/bin/python3
"""
    Python script that returns information using a REST API
"""


if __name__ == "__main__":
    import requests
    import sys

    url = 'https://jsonplaceholder.typicode.com/users/'
    empId = sys.argv[1]
    reqName = requests.get(url + empId)
    reqTodos = requests.get(url + empId + '/todos/')
    total = 0
    completed = 0
    tasks = []
    for elem in (reqTodos.json()):
        if ((elem['completed']) is True):
            completed += 1
            total += 1
            tasks.append(elem['title'])
        else:
            total += 1
    print('Employee {} is done with tasks ({}/{}):'.format(
          (reqName.json()).get('name'), completed, total))
    for t in tasks:
        print(f"\t{t}")
