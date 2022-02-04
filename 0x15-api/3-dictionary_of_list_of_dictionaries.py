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

    reqAllTodos = requests.get("https://jsonplaceholder.typicode.com/users/")
    uid = 1
    newList = []
    while (uid <= len(reqAllTodos.json())):
        reqUIDTodos = requests.get(url + str(uid) + "/todos/")
        newDict = {}
        for elem2 in (reqUIDTodos.json()):
            dictTask = {}
            dictTask["task"] = elem2["title"]
            if ((elem2["completed"]) is True):
                dictTask["completed"] = True
            else:
                dictTask["completed"] = False
            dictTask["username"] = (requests.get(url + str(uid))).json().get("username")
            newList.append(dictTask)
        newDict[uid] = newList
        uid += 1
    with open(sys.argv[1] + ".json", "w") as f:
        f.write(json.dumps(newDict))
        f.close
