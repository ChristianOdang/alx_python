""" 
Module that use PAT to access the Github api
"""

import sys
import requests


username = str(sys.argv[1])
token = str(sys.argv[2])
url = f'https://api.github.com/users/{username}'
parameters = (username, password)

response = requests.get(url, auth=parameters)
try:
    print(response.json()['id'])
except:
    print('None')


