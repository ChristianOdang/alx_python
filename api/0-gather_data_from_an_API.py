""" 
This script uses an API to retrieve employees task information
and display it in a special format.

It retrieves employees name, task completed with their title.
"""
import requests
import sys

# No execution of this file when imported
if __name__ == "__main__":

    # Pass employees id on command line
    id = sys.argv[1]

    # APIs
    userTodoURL = "https://jsonplaceholder.typicode.com/users{}/todos".format(
        id)
    userProfile = "https://jsonplaceholder.typicode.com/users/{}".format(id)

    # Make requests on APIs
    todoResponse = requests.get(userTodoURL)
    profileResponse = requests.get(userProfile)

    # Get employees information
    employeeName = profileJson_Data['name']

    # Count total and completed task
    totalTasks = 0
    completedTasks = 0

    for data in todoJson_Data:
        for key, value in data.item():
            if key == 'completed':
                totalTasks += 1
                if value == True:
                    completedTasks += 1

print("Employees {} is done with "
      "tasks({}/{}):".format(employeeName, completedTasks, totalTasks))

# Retrieve title of completed tasks
for data in todoJson_Data:
    for key, value in data.items():
        if key == 'completed' and value == True:
            print("\t {}".format(data['title']))
