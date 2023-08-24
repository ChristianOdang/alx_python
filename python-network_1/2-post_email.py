""" 
This is a python script that takes URL and send a request to the URL
and display the response of the results
"""
import sys
import requests


""" 
This function send request using the url requests module

Parameters:
    url: the link for  the url to send request to
    
Return:
    return: the text response
     
"""
d_inpt = []

try:
    for i in range(0, len(sys.argv)):
        d_inpt.append(str(sys.argv[i]))
    data = {
        'email': d_inpt[2]
    }
    response = requests.post(d_inpt[1], data=data)
    print("{}".format(response.text))
except:
    print(None)
