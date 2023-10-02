""" 
This script uses an API to retrieve employees task information
and display it in a special format.

It retrieves employees name, task completed with their title.
"""
import requests
import sys
import csv

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

    # Parse responses and store in variables
    todoJson_Data = todoResponse.json()
    profileJson_Data = profileResponse.json()

    # Get employee information
    employeeName = profileJson_Data['name']

    dataList = []

    for data in todoJson_Data:
        dataDict = {
            "userId": data['userId'], "name": employeeName, "completed": data['completed']}
        dataList.append(dataDict)

    # Specify the CSV file path
    csv_file_path = '{}.csv'.format(id)

    # Define the field names (column header)
    fieldnames = ["userId", "name", "completed", "title"]

    # Open the CSV file in write mode
    with open(csv_file_path, 'w', newline='') as csv_file:
        # Create a CSV writer
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write the data rows
        for row in dataList:
            csv_writer.writerow(row)
