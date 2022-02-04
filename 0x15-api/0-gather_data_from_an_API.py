#!/usr/bin/python3
"""Python script that returns information using a REST API"""


if __name__ == "__main__":
    import requests
    import sys

    url = 'https://jsonplaceholder.typicode.com/users/'
    empId = sys.argv[1]
    urlName = url + empId
    urlTodos = url + empId + '/todos/'

    reqName = requests.get(urlName)
    reqTodos = requests.get(urlTodos)
    
    reqNameJSON = reqName.json()
    reqTodosJSON = reqTodos.json()
    
    total = 0
    completed = 0
    tasks = []
    name = reqNameJSON.get('name')

    for elem in (reqTodosJSON):
        if ((elem['completed']) is True):
            completed += 1
            total += 1
            tasks.append(elem['title'])
        else:
            total += 1
    
    print('Employee {} is done with tasks ({}/{}):'.format(
          name, completed, total))
    
    for t in tasks:
        print(f"\t{t}")
