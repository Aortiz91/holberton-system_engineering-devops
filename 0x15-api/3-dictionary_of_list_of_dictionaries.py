#!/usr/bin/python3
""" Python script that gets API info and exports it to JSON """
import json
import requests
import sys

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/users/"
    reqAllTodos = requests.get("https://jsonplaceholder.typicode.com/users/")
    uid = 1
    newList = []
    while (uid <= len(reqAllTodos.json())):
        reqUIDTodos = requests.get(url + str(uid) + "/todos/")
        newDict = {}
        for elem2 in (reqUIDTodos.json()):
            dictTask = {}
            dictTask["username"] = (
                     requests.get(url + str(uid))).json().get("username")
            dictTask["task"] = elem2["title"]
            if ((elem2["completed"]) is True):
                dictTask["completed"] = True
            else:
                dictTask["completed"] = False
            newList.append(dictTask)
            print(newList)
        newDict[uid] = newList
        uid += 1
    with open("todo_all_employees.json", "w") as f:
        f.write(json.dumps(newDict))
        f.close
