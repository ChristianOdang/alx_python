""" 
This script uses an API to retrieve employees task information
and display it in a special format.

"""

"""
This script uses an API to retrieve employee task information
and display in a special format.

It retrieves employees name, task completed with their titles.
"""
import json
import requests
import sys

# No execution of this file when imported
if __name__ == "__main__":
    
# Pass employee id on command line
    id = sys.argv[1]

# APIs 
    userTodoURL = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    userProfile = "https://jsonplaceholder.typicode.com/users/{}".format(id)

# Make requests on APIs
    todoResponse = requests.get(userTodoURL)
    profileResponse = requests.get(userProfile)

# Parse responses and store in variables
    todoJson_Data = todoResponse.json()
    profileJson_Data = profileResponse.json()

#Get employee information
    employeeName = profileJson_Data['username']

    dataList = []# Empty list to store the dictionaries

    for data in todoJson_Data:
        dataDict = {"task":data['title'], "completed":data['completed'], "username":employeeName}
        dataList.append(dataDict)

# A dictionary of list of dictionaries to be exported to JSON
    outputData = {profileJson_Data['id']: dataList}

# Specify the JSON file path
    json_file_path = '{}.json'.format(todoJson_Data[0]['userId'])

# Open the JSON file in write mode
    with open(json_file_path, 'w') as json_file:
    # Serialize and write the data to the JSON file
        json.dump(outputData, json_file)
