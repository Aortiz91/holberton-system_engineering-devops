#!/usr/bin/python3
""" Python script that gets API info and exports it to CSV """
import requests
import sys
import csv

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
    with open(sys.argv[1] + ".csv", "a") as f:
        for elem2 in (reqTodos.json()):
            f.write("\"")
            f.write(str(elem2["userId"]))
            f.write("\",\"")
            f.write(str(name))
            f.write("\",\"")
            f.write(str(elem2["completed"]))
            f.write("\",\"")
            f.write(str(elem2["title"]))
            f.write("\"\n")
        f.close
