#!/usr/bin/python3
""" Python script that gets API info and exports it to JSON """
import json
import requests
import sys

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/users/"
    reqName = requests.get(url + sys.argv[1])
    reqTodos = requests.get(url + sys.argv[1] + "/todos/")
    name = reqName.json().get("name")
    total = 0
    comp = 0
    tasks = []
    for elem in (reqTodos.json()):
        if ((elem["completed"]) is True):
            comp += 1
            total += 1
            tasks.append(elem["title"])
        else:
            total += 1
    print("Employee {} is done with tasks({}/{}):".format(name, comp, total))
    for t in tasks:
        print("\t {}". format(t))
    newList = []
    newDict = {}
    for elem2 in (reqTodos.json()):
        dictTask = {}
        dictTask["task"] = elem2["title"]
        if ((elem2["completed"]) is True):
            dictTask["completed"] = "true"
        else:
            dictTask["completed"] = "false"
        dictTask["username"] = reqName.json().get("username")
        newList.append(dictTask)
    newDict[sys.argv[1]] = newList
    with open(sys.argv[1] + ".json", "w") as f:
        f.write(json.dumps(newDict))
        f.close
