""" 
This is a Python script that takes URL and send a request to the url
and display the response of the results.
"""
import sys
import requests


""" 
This function send request using the url requests module

Parameters:
    URL: the link to the url to send request to
    
Return:
    return: the text response
    
"""

url = sys.argv[1]
response = requests.get(url)
if response.status_code >= 400:
    print("Error code:", response.status_code)
else:
    print(response)
