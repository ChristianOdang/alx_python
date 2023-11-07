"""
This script uses an API to retrieve employee task information
and display in a special format.

It retrieves employees name, task completed with their titles.
"""
import json
import requests

# No execution of this file when imported
if __name__ == "__main__":

    
    outputDict = {}
    for i in range(1, 11):
        task_list = []
        userProfile = "https://jsonplaceholder.typicode.com/users/{}".format(i)
        profile_response = requests.get(userProfile).json()
        user_id = profile_response['id']
        username = profile_response['username']

        userTodoURL = "https://jsonplaceholder.typicode.com/users/{}/todos".format(i)
        todo_response = requests.get(userTodoURL).json()

        for task in todo_response:
            
            dataDict = {"username":username, "task":task['title'], "completed":task['completed']}
            task_list.append(dataDict)
        
        outputDict[user_id] = task_list

    # Specify the JSON file path
    json_file_path = 'todo_all_employees.json'

# Open the JSON file in write mode
    with open(json_file_path, 'w') as json_file:
    # Serialize and write the data to the JSON file
        json.dump(outputDict, json_file)
