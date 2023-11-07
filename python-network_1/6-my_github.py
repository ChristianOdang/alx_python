"""
 Python script that takes your GitHub credentials
   (username and password) and uses the GitHub API to display your id
"""
import sys 
import requests

url = 'https://api.github.com/user'
username = sys.argv[1]
password = sys.argv[2]
parameters = (username, password)

response = requests.get(url, auth=parameters)
try:
    print(response.json()['id'])
except:
    print('None')
