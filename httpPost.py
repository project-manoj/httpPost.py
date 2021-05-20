#!/usr/bin/python3.9
import requests
import json

# JSON data in form of Json Array is stored in jsonDataFile
datafile = open("jsonDataFile", "r")
data = json.load(datafile)
numentry = 0
URL = "http://example.com/api/v1/hssMap/addUser"
# print(data)
newHeaders = {"Content-type": "application/json", "Accept": "*/*"}

for pui in data:
    # print(f"DB entry for {pui}")
    response = requests.request(
        "POST",
        URL,
        json=pui,
        headers=newHeaders,
    )
    resp = response.json()
    print("Status code: ", response.status_code)
    if response.status_code != 200:
        print(f"Failed: {resp}\n")
    else:
        numentry += 1
        print(f"{pui['PUI']} added to DB")

print(f"Total Number of successful post entries: {numentry}")
